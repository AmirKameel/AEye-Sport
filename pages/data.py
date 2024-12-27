import streamlit as st
import openai
import os
import speech_recognition as sr
from moviepy.editor import VideoFileClip
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# Load OpenAI API key from secrets.toml
openai_api_key = st.secrets["openai"]["api_key"]
client = openai.OpenAI(api_key=openai_api_key)

# Set up the upload directory
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

st.title("Video Transcription App")
st.write("Upload a video file or provide a YouTube URL to transcribe the audio.")

# Choose input method
option = st.selectbox("Choose input method:", ["YouTube URL", "Upload Video File"])

# Function to extract audio from video file
def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = video_path.replace('.mp4', '.wav')
    video.audio.write_audiofile(audio_path)
    video.close()
    return audio_path

# Function to transcribe audio with Whisper API (Arabic)
def transcribe_audio_with_whisper(audio_file):
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language="ar"
    )
    return transcription.text

# Function to transcribe audio with Google Speech Recognition (English)
def transcribe_audio_with_google(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            transcription = recognizer.recognize_google(audio, language="en-US")
        except sr.UnknownValueError:
            transcription = "Could not understand audio"
        except sr.RequestError:
            transcription = "Could not request results"
    return transcription

# Function to split text into chunks
def split_text_into_chunks(text, chunk_size=2000):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 <= chunk_size:
            current_chunk.append(word)
            current_length += len(word) + 1
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word) + 1

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

# Function to split text with timestamps
def split_text_with_timestamps(transcript, chunk_size=1000):
    chunks = []
    current_chunk = ""
    current_start_time = None

    for item in transcript:
        text = item['text']
        start_time = item['start']
        if current_start_time is None:
            current_start_time = start_time

        # Check if adding this text would exceed the chunk size
        if len(current_chunk) + len(text) > chunk_size:
            # If so, save the current chunk and reset
            chunks.append((current_start_time, current_chunk.strip()))
            current_chunk = text
            current_start_time = start_time
        else:
            current_chunk += " " + text

    # Append any remaining text as the last chunk
    if current_chunk:
        chunks.append((current_start_time, current_chunk.strip()))

    return chunks

# Format time in 'HH:MM:SS'
def format_time(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hrs:02}:{mins:02}:{secs:02}"


# Function to analyze selected chunks with custom prompt
def analyze_chunks_with_gpt(chunks, custom_prompt):
    combined_text = " ".join(chunks)
    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant helping to analyze specific portions of text."
                " The user will provide selected chunks of text along with a custom prompt."
                " Please focus on the instructions in the prompt and provide a concise and relevant analysis."
            )
        },
        {
            "role": "user",
            "content": (
                f"{custom_prompt}\n\n"
                "Here is the combined text of the selected chunks:\n\n"
                f"{combined_text}"
            )
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=4000
    )
    return response.choices[0].message.content

# Process YouTube URL input
if option == "YouTube URL":
    youtube_url = st.text_input("Paste YouTube URL here:")
    if youtube_url:
        try:
            video_id = YouTube(youtube_url).video_id
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'ar'])

            chunks = split_text_with_timestamps(transcript)
            selected_chunks = []
            st.write("Transcription in Chunks with Timestamps:")
            for idx, (start_time, chunk) in enumerate(chunks):
                formatted_time = format_time(start_time)
                if st.checkbox(f"Select Chunk {idx + 1} ({formatted_time})", key=f"chunk_{idx}"):
                    selected_chunks.append(chunk)
                st.text_area(f"Chunk {idx + 1} ({formatted_time})", chunk, height=250)

        except Exception as e:
            st.error(f"Error: {e}")

# Process Video Upload input
elif option == "Upload Video File":
    uploaded_video = st.file_uploader("Upload a video file (mp4 format)", type=["mp4"])
    language = st.selectbox("Select transcription language", ("English", "Arabic"))

    if uploaded_video:
        video_path = os.path.join(UPLOAD_FOLDER, uploaded_video.name)
        with open(video_path, "wb") as f:
            f.write(uploaded_video.getbuffer())

        audio_path = extract_audio(video_path)

        # Use Whisper API for Arabic, and Google Speech Recognition for English
        if language == "Arabic":
            with open(audio_path, "rb") as audio_file:
                transcription_text = transcribe_audio_with_whisper(audio_file)
        else:
            transcription_text = transcribe_audio_with_google(audio_path)

        # Split transcription into chunks with timestamps
        transcript = [{"text": transcription_text, "start": 0}]  # Simulate single block for non-timestamped transcript
        chunks = split_text_with_timestamps(transcript)
        selected_chunks = []
        st.write("Transcription in Chunks with Timestamps:")
        for idx, (start_time, chunk) in enumerate(chunks):
            formatted_time = format_time(start_time)
            if st.checkbox(f"Select Chunk {idx + 1} ({formatted_time})", key=f"chunk_{idx}"):
                selected_chunks.append(chunk)
            st.text_area(f"Chunk {idx + 1} ({formatted_time})", chunk, height=250)

        # Clean up files
        if os.path.exists(video_path):
            os.remove(video_path)
        if os.path.exists(audio_path):
            os.remove(audio_path)

# Custom prompt input
st.write("Enter your custom prompt for GPT analysis:")
custom_prompt = st.text_area("Custom Prompt")

# Button to analyze selected chunks
if st.button("Analyze Selected Chunks"):
    if selected_chunks:
        result = analyze_chunks_with_gpt(selected_chunks, custom_prompt)
        st.write("GPT Analysis Result:")
        st.text_area("Analysis Result", result, height=300)
    else:
        st.warning("Please select at least one chunk for analysis.")