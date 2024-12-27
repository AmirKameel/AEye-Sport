import streamlit as st
import pandas as pd
import os
import openai

# Set up page configuration
st.set_page_config(page_title="Player Performance Analysis", page_icon="⚽", layout="wide")




# Navigation bar setup remains the same
pages = ["Home", "Player", "Team", "A_Eye"]
urls = {"A_Eye": "aeye-sport.com"}

styles = {
    "nav": {
        "background-color": "#2C3E50",
        "justify-content": "center",
        "padding": "10px",
        "border-radius": "5px",
        "box-shadow": "0px 4px 8px rgba(0,0,0,0.2)"
    },
    "img": {"padding-right": "14px"},
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
options = {"show_menu": False}

# Save uploaded file
def save_uploaded_file(uploaded_file, file_path):
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

# Analyze performance using GPT-3.5
def analyze_performance(file_path, player_name):
    try:
        # Read the data
        data = pd.read_csv(file_path)
        player_data = data[data["Name"] == player_name]

        if player_data.empty:
            st.error(f"Player '{player_name}' not found in the uploaded file.")
            return None

        # Get all available statistics for the player
        stats = {column: player_data[column].iloc[0] for column in player_data.columns if column != "Name"}

        # Create prompt for AI analysis
        prompt = f"I need you to be a professional football performance analyst. Please analyze the performance and extract the strengths and weaknesses of player {player_name} based on these statistics:\n"
        for stat, value in stats.items():
            prompt += f"- {stat}: {value}\n"
        prompt += "\nPlease provide the analysis in this format:\n"
        prompt += "1. Overall Performance Summary\n"
        prompt += "2. Key Strengths (minimum 3)\n"
        prompt += "3. Areas for Improvement (minimum 2)\n"
        prompt += "4. Specific Performance Metrics Analysis\n"
        prompt += "5. Development Recommendations\n"
        prompt += """and here is a html templete i need you to edit it based on the player performancce then return all the templete i need you to make detailed report if you want to add more sections do it at the end just return the code without any strings like that '''html at begin or end 
          <!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>تحليل أداء مهند لاشين</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"/>
  <style>
    .fade-in {
      animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
  </style>
</head>
<body class="bg-gray-100 font-roboto">
  <div class="container mx-auto p-4">
    <div class="bg-white shadow-lg rounded-lg p-6 fade-in">
      <div class="flex items-center mb-6">
        <img alt="لوجو الشركه الصمنعه" class="rounded-full w-24 h-24 mr-4" height="100" src="https://aeye-sport.com/wp-content/uploads/2024/10/aeye.jpg" width="100"/>
        <div>
          <h1 class="text-4xl font-bold">
            تحليل أداء مهند لاشين في الشوط الثاني
          </h1>
        </div>
      </div>
      <div class="grid grid-cols-1 gap-4">
        <div class="bg-blue-100 p-4 rounded shadow-md">
          <h3 class="text-2xl font-bold mb-4 text-blue-600">
            الأداء العام
          </h3>
          <p class="text-gray-700 text-lg">
            في الشوط الثاني، كان مهند لاشين لاعبًا مهمًا في صفوف فريق بيراميدز. قدم أداءً متوازنًا، حيث ساهم في بناء الهجمات والدفاع.
          </p>
        </div>
        <div class="bg-green-100 p-4 rounded shadow-md">
          <h3 class="text-2xl font-bold mb-4 text-green-600">
            نقاط القوة
          </h3>
          <ul class="list-disc list-inside text-gray-700">
            <li class="mb-2">
              <strong>
                التمريرات الدقيقة:
              </strong>
              أظهر مهند دقة في التمريرات، حيث كان يوزع الكرة بشكل جيد بين زملائه، مما ساعد في الحفاظ على الاستحواذ وخلق فرص جديدة.
            </li>
            <li class="mb-2">
              <strong>
                التحركات الذكية:
              </strong>
              قام بتحركات ذكية داخل الملعب، مما ساعده على استغلال المساحات الفارغة. كان يتواجد في الأماكن المناسبة لتلقي الكرة، مما زاد من فعالية الهجمات.
            </li>
            <li class="mb-2">
              <strong>
                القدرة على استعادة الكرة:
              </strong>
              كان نشطًا في الضغط على لاعبي الجيش الرواندي، مما ساعد في استعادة الكرة في مناطق متقدمة. هذا الضغط ساهم في إرباك دفاع الخصم.
            </li>
            <li class="mb-2">
              <strong>
                القدرة على التمرير تحت الضغط:
              </strong>
              أظهر قدرة جيدة على التمرير تحت الضغط، حيث تمكن من الحفاظ على هدوئه في المواقف الصعبة وتمرير الكرة بدقة.
            </li>
          </ul>
        </div>
        <div class="bg-red-100 p-4 rounded shadow-md">
          <h3 class="text-2xl font-bold mb-4 text-red-600">
            نقاط الضعف
          </h3>
          <ul class="list-disc list-inside text-gray-700">
            <li class="mb-2">
              <strong>
                الإرهاق في الدقائق الأخيرة:
              </strong>
              مع تقدم المباراة، بدا أن مهند يعاني من الإرهاق، مما أثر على سرعته وقدرته على المشاركة في الهجمات. كان من الممكن أن يؤثر ذلك على فعاليته في الدقائق الأخيرة.
            </li>
            <li class="mb-2">
              <strong>
                عدم القدرة على إنهاء الهجمات:
              </strong>
              على الرغم من تقديمه لتمريرات جيدة، إلا أن مهند لم يكن فعالًا في إنهاء الهجمات بنفسه. كان هناك بعض الفرص التي كان يمكنه استغلالها بشكل أفضل.
            </li>
            <li class="mb-2">
              <strong>
                التعرض للضغط من الخصم:
              </strong>
              في بعض الأحيان، تعرض للضغط من لاعبي الجيش الرواندي، مما أدى إلى فقدان الكرة في مواقف حرجة. كان من الممكن أن يكون أكثر حذرًا في تلك اللحظات.
            </li>
          </ul>
        </div>
        <div class="bg-yellow-100 p-4 rounded shadow-md">
          <h3 class="text-2xl font-bold mb-4 text-yellow-600">
            الخلاصة
          </h3>
          <p class="text-gray-700 text-lg">
            قدم مهند لاشين أداءً جيدًا في الشوط الثاني، حيث كان له دور فعال في بناء الهجمات والضغط على الخصم. ومع ذلك، يحتاج إلى تحسين قدرته على إنهاء الهجمات وتجنب فقدان الكرة تحت الضغط.
          </p>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
 """

        # Call GPT-3.5 for analysis
        from openai import OpenAI

        import toml

# Load API key from secrets.toml
        openai_api_key = st.secrets["openai"]["api_key"]
        client = openai.OpenAI(api_key=openai_api_key)       
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional football performance analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        analysis_result = response.choices[0].message.content

        # Read HTML template


        return analysis_result

    except Exception as e:
        st.error(f"Error processing file: {e}")
        return None


# Streamlit UI
st.markdown("""
    <style>
        .section-title {
            color: #2C3E50;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .section-subtitle {
            color: #2C3E50;
            font-size: 24px;
            margin-bottom: 10px;
        }
        .analysis-result {
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='section-title'>Player Performance Analysis</h1>", unsafe_allow_html=True)

# File upload section
st.markdown("<h2 class='section-subtitle'>Upload Player Stats File (CSV)</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type="csv")

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        temp_dir = "temp_files"
        os.makedirs(temp_dir, exist_ok=True)
        
        csv_file_path = os.path.join(temp_dir, "temp_data.csv")
        save_uploaded_file(uploaded_file, csv_file_path)
        
        # Display CSV structure
        df = pd.read_csv(csv_file_path)
        st.write("Available statistics in your data:")
        st.write(df.columns.tolist())
        
        player_names = df["Name"].tolist()
        selected_player = st.selectbox("Select Player", ["-- Select Player --"] + player_names)

        # HTML template upload
        #st.markdown("<h2 class='section-subtitle'>Upload HTML Template</h2>", unsafe_allow_html=True)
       #template_file = st.file_uploader("", type=["html"])

        if selected_player != "-- Select Player --":
            #template_path = os.path.join(temp_dir, "template.html")
            #save_uploaded_file(template_file, template_path)

            if st.button("Analyze Performance"):
                analysis_result= analyze_performance(
                    csv_file_path, 
                    selected_player, 
                    #template_path
                )
                
                if analysis_result:
                    st.markdown("<div class='analysis-result'>", unsafe_allow_html=True)
                    st.markdown("<h2 class='section-subtitle'>Performance Analysis</h2>", unsafe_allow_html=True)
                    #st.write(analysis_result)
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    st.markdown("<h2 class='section-subtitle'>Download Report</h2>", unsafe_allow_html=True)
               
                    st.download_button(
                        label="Download Report", 
                        data=analysis_result, 
                        file_name=f"{selected_player}_analysis.html", 
                        mime="text/html"
                    )