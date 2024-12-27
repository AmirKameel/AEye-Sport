import streamlit as st
import pandas as pd
import os
import openai
from streamlit_navigation_bar import st_navbar

# Set up page configuration
st.set_page_config(page_title="Player Performance Analysis", page_icon="⚽", layout="wide")

# Define pages and their respective URLs
pages = ["Home", "Player", "Team", "A_Eye"]
urls = {"A_Eye": "https://aeye-sport.com/"}

# Styles for the navigation bar
styles = {
    "nav": {
        "background-color": "#2C3E50",  # Dark blue
        "justify-content": "center",
        "padding": "10px",
        "border-radius": "5px",
        "box-shadow": "0px 4px 8px rgba(0,0,0,0.2)"
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "font-weight": "bold",
        "padding": "14px",
        "font-size": "18px"
    },
    "active": {
        "background-color": "white",
        "color": "#2C3E50",
        "font-weight": "bold",
        "padding": "14px",
        "border-radius": "5px",
        "box-shadow": "0px 4px 8px rgba(0,0,0,0.1)"
    }
}
options = {
    "show_menu": False,
}

page = st_navbar(
    pages,
    urls=urls,
    styles=styles,
    options=options,
    selected="Team"
)

if page == "Home":
    st.switch_page("home.py")
if page == "Player":
    st.switch_page("pages/player.py")



def save_uploaded_file(uploaded_file, file_path):
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

def analyze_team_data(data, team_name):
    try:
        # Normalize team names for better matching
        data['Team'] = data['Team'].str.strip().str.lower()

        # Select data for the chosen team
        team_data = data[data["Team"] == team_name]
        if team_data.empty:
            return f"No data available for the team: {team_name}"

        # Convert the selected team data into a dictionary
        team_stats = team_data.to_dict(orient="list")

        # Build a dynamic prompt based on the uploaded data
        prompt = f"Analyze the performance of the team '{team_name}' based on the following data:\n"
        for column, values in team_stats.items():
            prompt += f"- {column}: {', '.join(map(str, values))}\n"
        from openai import OpenAI

        import toml

# Load API key from secrets.toml
        openai_api_key = st.secrets["openai"]["api_key"]
        client = openai.OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are an expert sports analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        analysis_result = response.choices[0].message.content

        return analysis_result

    except Exception as e:
        st.error(f"Error processing data: {e}")
        return None

st.title("Football Performance Analyzer (Flexible Data Upload)")

uploaded_file = st.file_uploader("Upload Team Stats File (CSV)", type="csv")
team_selected = None

if uploaded_file is not None:
    try:
        # Read uploaded file
        data = pd.read_csv(uploaded_file)

        # Normalize team names for dropdown
        data['Team'] = data['Team'].astype(str).str.strip().str.lower()
        unique_teams = data['Team'].unique()

        team_selected = st.selectbox("Select Team Name", options=unique_teams)

        if team_selected:
            if st.button("Analyze Team Performance"):
                with st.spinner('Analyzing...'):
                    analysis_result = analyze_team_data(data, team_selected)
                    if analysis_result:
                        st.markdown("## Team Performance Analysis")
                        st.write(analysis_result)
                    else:
                        st.warning("Analysis failed. Please check the data and try again.")
    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Please upload a CSV file containing team stats.")