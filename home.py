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
        "padding": "5px",
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
    st.write("Hi")


#if page == "Talent":
 #   st.switch_page("pages/player.py")
if page == "Player":
    st.switch_page("pages/player.py")
if page == "Team":
    st.switch_page("pages/team.py") 
