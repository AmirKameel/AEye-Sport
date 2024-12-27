import os
import streamlit as st
from streamlit_navigation_bar import st_navbar

# Set up page configuration
st.set_page_config(page_title="A_Eye Football Performance Analysis", page_icon="⚽", layout="wide")

# Define pages and their respective URLs
pages = ["Home", "Player", "Team", "A_Eye"]
urls = {"A_Eye": "https://aeye-sport.com"}

# Styles for the navigation bar
styles = {
    "nav": {
        "background-color": "#2C3E50",  # Dark blue
        "justify-content": "center",
        "padding": "20px",  # Increased padding to move it down
        "margin-top": "20px",  # Add margin to push the navbar down
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
    "show_sidebar": False,
}

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
    st.markdown("""<style>
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
    st.markdown("""<style>
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


#if page == "Talent":
 #   st.switch_page("pages/player.py")
if page == "Player":
    st.switch_page("pages/player.py")
if page == "Team":
    st.switch_page("pages/team.py") 
