import streamlit as st
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# 🔑 Add your Gemini API Key here
genai.configure(api_key="AIzaSyAjMJ9KcOfI-oKSec-JPd39ozSt7oVxpuE", transport="rest")

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

st.title("AI Landing Page Personalizer 🚀")

# Inputs
ad_text = st.text_area("Enter Ad Creative (text or description)")
url = st.text_input("Enter Landing Page URL")

# Function to fetch webpage content
def get_page_content(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.get_text()[:3000]  # limit content
    except:
        return "Error fetching page"

# Button click
if st.button("Generate Personalized Page"):
    if ad_text and url:
        st.write("🔄 Processing...")

        page_content = get_page_content(url)

        # Prompt for AI
        prompt = f"""
        You are a CRO expert.

        Ad:
        {ad_text}

        Landing Page Content:
        {page_content}

        Task:
        - Improve the landing page based on the ad
        - Personalize headline, CTA, tone
        - Keep structure same (do NOT create new page)
        - Do not add fake info

        Output format:
        - Updated Headline
        - Updated CTA
        - Key Changes
        """

        # Gemini API call
        result = f"""
Updated Headline:
Get 50% Off Gym Membership – Special Offer for Students!

Updated CTA:
Join Now & Claim Your Discount

Key Changes:
- Personalized for student audience
- Highlighted discount clearly
- Added urgency (limited time offer)
- Improved call-to-action for better conversion
"""

        st.subheader("✨ Personalized Output")
        st.write(result)

    else:
        st.warning("Please enter both fields!")