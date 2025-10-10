# 🧠 AI GCSE Biology Marker (Streamlit Prototype)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-app-success)
[![Live Demo](https://img.shields.io/badge/🌐%20Live-Demo-brightgreen)](https://ai-gcse-marker-prototype.streamlit.app/)

A **Streamlit-based AI marking prototype** that evaluates short GCSE Biology answers using OpenAI’s GPT models and prompt-engineered marking logic.  
It automatically produces:
- ✅ **Awarded Mark / Max Mark**
- 🧩 **Structured Feedback** – what was correct or missing  
- 💡 **Exam Tip** – how to improve next time  

> ⚙️ **Status:** Stable locally · Deployed on [Streamlit Cloud](https://ai-gcse-marker-prototype.streamlit.app/)

---

## 🚀 Features
- 🎓 **AI marking engine** based on GPT-4o  
- 🧠 **Prompt-engineered grading logic** aligned to GCSE mark schemes  
- 🧾 **Google Sheets integration** (optional) for logging answers  
- 🌱 **Lightweight Streamlit UI** for quick student testing  
- 🔐 Simple environment setup with `.env.example`

---

## 🧰 Tech Stack
**Python**, **Streamlit**, **OpenAI API**, **pandas**, **gspread / Google Sheets API**

---


```markdown
📦 Quickstart
bash
Copy code
# 1️⃣ Clone the repo and install dependencies
git clone https://github.com/Salama-Khan/ai-gcse-biology-marker.git
cd ai-gcse-biology-marker
pip install -r requirements.txt

# 2️⃣ Add your environment variables
cp .env.example .env
# Fill in your OpenAI key and (optionally) Google Sheets credentials

# 3️⃣ Run the app
streamlit run app/app.py

📚 Environment Variables
Variable	Description
OPENAI_API_KEY	Your OpenAI API key
GOOGLE_SHEET_KEY	(Optional) Your Google Sheet ID
G_SERVICE_JSON	(Optional) Google service account credentials JSON

📝 License
This project is licensed under the MIT License.

💬 Support / Issues
Found a bug or have a suggestion?
Open an issue or reach out via email.

Live App: ai-gcse-marker-prototype.streamlit.app
Created by: Salama Khan