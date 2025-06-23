import streamlit as st
import pandas as pd
import openai
import re
import os
import datetime
import csv
import gspread
import json
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_FILE = 'credentials.json'  # <-- Your downloaded key file
SHEET_NAME = 'Research Log AI Marker'  # <-- Must match the sheet name exactly
SHEET_KEY = st.secrets["GOOGLE_SHEET_KEY"]

scope = ['https://www.googleapis.com/auth/spreadsheets',]
gdrive_creds = json.loads(st.secrets["G_SERVICE_JSON"])
creds = Credentials.from_service_account_info(gdrive_creds, scopes=scope)
gc = gspread.authorize(creds)
sheet = gc.open_by_key(SHEET_KEY).sheet1


url = "https://raw.githubusercontent.com/Salama-Khan/scaling-guide/main/streamlit%20prototype/question_bankbio.csv"
question_df = pd.read_csv(url)


client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def clean_text(text):
    return text.replace("\n", " ").replace("\r", " ").strip()

def extract_max_mark(row):
    return row["max_marks"]

def save_results_to_google_sheets(question_text, student_answer, awarded, max_marks, feedback, exam_tip):
    new_row = [
        str(datetime.datetime.now().isoformat()),
        str(question_text),
        str(student_answer),
        str(awarded),
        str(max_marks),
        str(feedback),
        str(exam_tip)
    ]
    sheet.append_row(new_row)

st.title("AI GCSE Biology Marker")
st.write("Select a topic and question to answer and get AI-generated marking.")


topics = question_df['topic'].unique()
selected_topic = st.selectbox("Choose a topic:", topics)

# sub_topics = question_df['sub_topic'].unique()
# selected_sub_topic = st.selectbox("Choose a sub topic:", sub_topics)

# questions_in_topic = question_df[question_df['sub_topic'] == selected_sub_topic]

questions_in_topic = question_df[question_df['topic'] == selected_topic]
question_texts = questions_in_topic['question_text'].tolist()

selected_question = st.selectbox("Select a question:", question_texts)
question_row = questions_in_topic[questions_in_topic['question_text'] == selected_question].iloc[0]
st.markdown(f"**Question:** {selected_question}")

question_text = question_row['question_text']
mark_scheme = question_row['mark_scheme']
max_marks = question_row['max_marks']


st.markdown(f"**Max Marks:** {question_row['max_marks']}")

student_answer = st.text_area("Enter your answer:")

SYSTEM_PROMPT = """
You are an expert GCSE Biology exam marker. Mark answers using the provided mark scheme.
Award only what is clearly earned, following official criteria strictly.

Use this format:

### Question:
{question}

### Mark Scheme:
{mark_scheme}

### Student Answer:
{student_answer}

### Marking:
| Criterion | Met? | Mark |
|-----------|------|------|
| (criterion 1) | Fully met / Not met | X |
| (criterion 2) | Fully met / Not met | X |

### Total Marks:
X / Total Marks

### Feedback:
{constructive_feedback}

### Exam Tip:
{one_improvement_tip}
"""

if st.button("Mark My Answer") and student_answer.strip():
    user_prompt = f"""
### Question:
{question_text}

### Mark Scheme:
{mark_scheme}

### Student Answer:
{student_answer}

### Marking:
| Criterion | Met? | Mark |
|-----------|------|------|
"""

    with st.spinner("Marking in progress..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0
        )

        output = response.choices[0].message.content
        st.markdown("## Marking Result")
        st.markdown(output)

        lines = output.splitlines()
        total_marks = ""
        feedback = ""
        exam_tip = ""
        current_section = None

        for line in lines:
            line = line.strip()
            if line.startswith("### Total Marks:"):
                current_section = "total_marks"
                continue
            elif line.startswith("### Feedback:"):
                current_section = "feedback"
                continue
            elif line.startswith("### Exam Tip:"):
                current_section = "exam_tip"
                continue

            if current_section and line:
                if current_section == "total_marks":
                    total_marks = line
                elif current_section == "feedback":
                    feedback = line
                elif current_section == "exam_tip":
                    exam_tip = line
                current_section = None

        awarded = total_marks.split("/")[0].strip() if total_marks else "0"

        if int(awarded) == int(max_marks):
            st.success(f"✅ Full marks! {total_marks}")
        elif int(awarded) == 0:
            st.error(f"❌ No marks awarded. {total_marks}")
        else:
            st.warning(f"⚠ Partial marks: {total_marks}")

        save_results_to_google_sheets(question_text, student_answer, awarded, max_marks, feedback, exam_tip)
        st.success("✅ Your answer has been saved to Google Sheets.")
