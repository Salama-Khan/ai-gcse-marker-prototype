# 🧠 AI GCSE Biology Marker (Streamlit Prototype)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **Streamlit-based AI marking prototype** that evaluates short GCSE Biology answers against a given mark scheme using prompt engineering.  
It provides:
- **Awarded Mark / Max Mark**
- **Structured Feedback** — what was correct or missing
- **Exam Tip** — how to improve next time

> ⚙️ Status: Working prototype — local version stable, Streamlit Cloud deployment in progress.

---

## 🚀 Features
- Simple, interactive **Streamlit UI**
- **OpenAI-based grading logic** via prompt engineering
- Optional **Google Sheets integration** for saving results
- Easy environment setup with `.env.example`

---

## 📦 Quickstart

```bash
# 1️⃣ Clone the repo and install dependencies
git clone https://github.com/Salama-Khan/ai-gcse-biology-marker.git
cd ai-gcse-biology-marker
pip install -r requirements.txt

# 2️⃣ Add your environment variables
cp .env.example .env
# Fill in your OpenAI key (and optional Google Sheet details)

# 3️⃣ Run the app
streamlit run app/app.py
