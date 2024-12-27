import streamlit as st
import base64
from pathlib import Path

# Page config
st.set_page_config(
    page_title="A_Eye Football Analysis",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with improved visibility and contrast
st.markdown("""
<style>
    /* Reset and base styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    [data-testid="stAppViewContainer"] {
        background: #0f172a;
    }

    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }

    .hero-title {
        color: #ffffff;
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }

    .hero-subtitle {
        color: #e2e8f0;
        font-size: 1.5rem;
        margin-bottom: 2rem;
    }

    /* Feature Cards */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        padding: 2rem 0;
    }

    .feature-card {
        background: linear-gradient(145deg, #1e3a8a 0%, #2563eb 100%);
        border-radius: 15px;
        padding: 2rem;
        color: white;
        transition: transform 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .feature-card:hover {
        transform: translateY(-10px);
    }

    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .feature-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #ffffff;
    }

    .feature-description {
        color: #e2e8f0;
        font-size: 1rem;
        line-height: 1.6;
    }

    /* Stats Section */
    .stats-section {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
        padding: 2rem 0;
    }

    .stat-card {
        background: linear-gradient(145deg, #1e3a8a 0%, #1e40af 100%);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        color: white;
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        color: #ffffff;
    }

    .stat-label {
        color: #e2e8f0;
        font-size: 1.1rem;
    }

    /* CTA Section */
    .cta-section {
        background: linear-gradient(145deg, #1e40af 0%, #3b82f6 100%);
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        margin: 2rem 0;
    }

    .cta-title {
        color: white;
        font-size: 2rem;
        margin-bottom: 1.5rem;
    }

    /* Button Styles */
    .custom-button {
        display: inline-block;
        padding: 1rem 2rem;
        margin: 0.5rem;
        background: #ffffff;
        color: #1e40af;
        text-decoration: none;
        border-radius: 10px;
        font-weight: bold;
        transition: all 0.3s ease;
        font-size: 1.1rem;
    }

    .custom-button:hover {
        background: #3b82f6;
        color: white;
        transform: translateY(-3px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    /* Footer */
    .footer {
        background: linear-gradient(145deg, #1e3a8a 0%, #1e40af 100%);
        color: white;
        padding: 2rem;
        text-align: center;
        border-radius: 15px;
        margin-top: 3rem;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .features-grid {
            grid-template-columns: 1fr;
        }
        
        .stats-section {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .hero-title {
            font-size: 2.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">A_Eye Football Analysis</h1>
    <p class="hero-subtitle">Revolutionizing Football Analytics with AI</p>
    <div>
        <a href="talent" class="custom-button">Talent Scout</a>
        <a href="player" class="custom-button">Player Analysis</a>
        <a href="team" class="custom-button">Team Analysis</a>
        <a href="https://aeye-sport.com" class="custom-button">A_Eye Platform</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Feature Cards
st.markdown("""
<div class="features-grid">
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <h3 class="feature-title">Talent Discovery</h3>
        <p class="feature-description">
            Leverage AI-powered analytics to identify promising talents and predict their potential with unprecedented accuracy.
        </p>
    </div>"""
           , unsafe_allow_html=True)
st.markdown("""    
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3 class="feature-title">Performance Analysis</h3>
        <p class="feature-description">
            Deep dive into comprehensive player statistics and performance metrics using advanced analytics tools.
        </p>
    </div>
    """ , unsafe_allow_html=True)
st.markdown(""""
    <div class="feature-card">
        <div class="feature-icon">⚽</div>
        <h3 class="feature-title">Team Intelligence</h3>
        <p class="feature-description">
            Optimize team strategies and make data-driven decisions with our cutting-edge team analysis platform.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Stats Section
st.markdown("""
<div class="stats-section">
    <div class="stat-card">
        <div class="stat-number">500+</div>
        <div class="stat-label">Teams Analyzed</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">10,000+</div>
        <div class="stat-label">Players Tracked</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">95%</div>
        <div class="stat-label">Prediction Accuracy</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">24/7</div>
        <div class="stat-label">Real-time Analysis</div>
    </div>
</div>
""", unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta-section">
    <h2 class="cta-title">Ready to Transform Your Football Analytics?</h2>
    <a href="https://aeye-sport.com" class="custom-button">Get Started Now</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <h3>A_Eye Football Analysis</h3>
    <p style="margin: 1rem 0;">Empowering football professionals with AI-driven insights</p>
    <p>© 2024 A_Eye Sports Analytics. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)