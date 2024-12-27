import os
import streamlit as st
from streamlit_navigation_bar import st_navbar

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

# Create the navigation bar
page = st_navbar(
    pages,
    urls=urls,
    styles=styles,
    options=options,
)

# Home Page Content
if page == "Home":
    # Header Section
    st.markdown("""
    <style>
    .header {
        text-align: center;
        padding: 50px;
        background: linear-gradient(to right, #2C3E50, #4CA1AF);
        color: white;
        border-radius: 10px;
    }
    .header h1 {
        font-size: 3em;
        margin-bottom: 10px;
    }
    .header p {
        font-size: 1.2em;
    }
    </style>
    <div class="header">
        <h1>Welcome to Football Performance Analysis</h1>
        <p>Analyze, Discover, and Scout Football Talent with AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero Image
    st.image("team2.jpeg", use_column_width=True)  # Replace with actual image URL
    
    # Service Overviews
    st.markdown("""
    <style>
    .services {
        display: flex;
        justify-content: space-around;
        padding: 30px 0;
    }
    .service {
        width: 30%;
        text-align: center;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        background-color: #f9f9f9;
        transition: transform 0.2s;
    }
    .service:hover {
        transform: scale(1.05);
    }
    .service img {
        width: 180px;
        height: 180px;
    }
    .service h2 {
        font-size: 1.5em;
        margin-top: 15px;
    }
    .service p {
        font-size: 1em;
        color: #555;
    }
    .service a {
        display: inline-block;
        margin-top: 10px;
        padding: 10px 20px;
        background-color: #2C3E50;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
    }
    .service a:hover {
        background-color: #4CA1AF;
    }
    </style>
    <div class="services">
        <div class="service">
            <img src="https://images.unsplash.com/photo-1526232761682-d26e03ac148e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGZvb3RiYWxsJTIwdGFsZW50fGVufDB8fDB8fHww" alt="Talent Icon">
            <h2>Scouting Young Talent</h2>
            <p>Discover the next football superstars with our AI-powered scouting tools.</p>
            <a href="talent">Explore Talent</a>
        </div>
        <div class="service">
            <img src="https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Zm9vdGJhbGwlMjBwbGF5ZXJ8ZW58MHx8MHx8fDA%3D" alt="Player Icon">
            <h2>Individual Player Analysis</h2>
            <p>Get detailed insights and performance metrics for individual players.</p>
            <a href="player">Analyze Player</a>
        </div>
        <div class="service">
            <img src="https://plus.unsplash.com/premium_photo-1685055940293-176c55f3e2b5?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Zm9vdGJhbGwlMjB0ZWFtfGVufDB8fDB8fHww" alt="Team Icon">
            <h2>Team Performance Analysis</h2>
            <p>Evaluate team dynamics and overall performance with advanced AI models.</p>
            <a href="team">Assess Team</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Feature Highlights
    st.markdown("""
    <style>
    .features {
        display: flex;
        justify-content: space-between;
        padding: 30px 0;
    }
    .feature {
        width: 30%;
        text-align: center;
    }
    .feature img {
        width: 180px;
        height: 180px;
    }
    .feature h3 {
        font-size: 1.2em;
        margin-top: 10px;
    }
    .feature p {
        font-size: 0.9em;
        color: #555;
    }
    </style>
    <div class="features">
        <div class="feature">
            <img src="https://media.istockphoto.com/id/1214728307/photo/two-business-graph-on-measure-grid.webp?b=1&s=170667a&w=0&k=20&c=z27RItlFSrcwFM-D379pTMCVU-mjS2az7xICkjHBQso=" alt="AI Icon">
            <h3>Advanced AI Algorithms</h3>
            <p>Leveraging cutting-edge AI to provide the most accurate insights and analysis.</p>
        </div>
        <div class="feature">
            <img src="https://media.istockphoto.com/id/610966386/photo/soccer-football-blue-board-concept.webp?b=1&s=170667a&w=0&k=20&c=hCDvYQFFbbORPGCIftil18otrcCLTv2LR9zIhM0-vlQ=" alt="Data Icon">
            <h3>Comprehensive Data</h3>
            <p>Access a wide range of data points for in-depth football analysis.</p>
        </div>
        <div class="feature">
            <img src="https://images.unsplash.com/photo-1434626881859-194d67b2b86f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Zm9vdGJhbGwlMjBkYXRhfGVufDB8fDB8fHww" alt="Report Icon">
            <h3>Detailed Reports</h3>
            <p>Generate detailed reports and visualizations for easy interpretation of results.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Call-to-Action
    st.markdown("""
    <style>
    .cta {
        text-align: center;
        margin-top: 50px;
        padding: 30px;
        background-color: #4CA1AF;
        color: white;
        border-radius: 10px;
    }
    .cta h2 {
        font-size: 2em;
    }
    .cta a {
        display: inline-block;
        margin-top: 20px;
        padding: 15px 30px;
        background-color: #2C3E50;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
    }
    .cta a:hover {
        background-color: #1ABC9C;
    }
    </style>
    <div class="cta">
        <h2>Get Started with AI-Driven Football Analysis</h2>
        <a href="/A_Eye">Start Now</a>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <style>
    .footer {
        position: relative;
        bottom: 0;
        width: 100%;
        background-color: #2C3E50;
        color: white;
        text-align: center;
        padding: 20px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        Developed by A_Eye Team | © 2024 Football Performance Analysis
    </div>
    """, unsafe_allow_html=True)


#if page == "Talent":
 #   st.switch_page("pages/player.py")
if page == "Player":
    st.switch_page("pages/player.py")
if page == "Team":
    st.switch_page("pages/team.py") 
