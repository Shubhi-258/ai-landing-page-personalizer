# AI Landing Page Personalizer 🚀

## 📌 Overview
This project is an AI-powered tool that personalizes landing page content based on an ad creative. It helps improve conversion rates using CRO (Conversion Rate Optimization) principles.

---

## 🎯 Features
- Input ad creative (text)
- Input landing page URL
- Extract webpage content
- Generate personalized headline, CTA, and improvements
- Simple and interactive UI using Streamlit

---

## ⚙️ Tech Stack
- Python
- Streamlit
- BeautifulSoup (for web scraping)

---

## 🔄 How It Works
1. User enters ad creative and landing page URL  
2. System extracts content from the webpage  
3. AI logic analyzes the ad  
4. Generates personalized output:
   - Updated Headline  
   - Call-to-Action (CTA)  
   - Key Changes  

---

## 🧠 Assumptions
- Ad input is provided as text  
- Landing page content is processed as plain text  
- Output focuses on content-level personalization  

---

## ⚠️ Limitations
- Does not modify full HTML structure  
- Prototype uses controlled output for consistency  

---

## 🚀 Future Improvements
- Full AI integration (OpenAI / Gemini APIs)  
- Real-time webpage editing  
- A/B testing support  
- UI enhancements  

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
