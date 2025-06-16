import streamlit as st
import pdfplumber
import json
import os

# Set page configuration
st.set_page_config(
    page_title="LexNova",
    page_icon="⚖️",
    layout="wide"
)

# Load JSON file
def load_json_file(json_path):
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            st.error(f"Error loading JSON file: {e}")
    else:
        st.error(f"File not found: {json_path}")
    return []

# Display PDF content
def display_pdf_content(uploaded_pdf):
    try:
        with pdfplumber.open(uploaded_pdf) as pdf:
            st.subheader("Judgement PDF Preview")
            for page_number, page in enumerate(pdf.pages, start=1):
                st.markdown(f"**Page {page_number}:**")
                text = page.extract_text()
                if text:
                    st.markdown(f"<pre>{text}</pre>", unsafe_allow_html=True)
                else:
                    st.warning("No text found on this page.")
                st.write("---")
    except Exception as e:
        st.error(f"Error processing PDF: {e}")

# Title and description
st.title("⚖️ LexNova")
st.caption(
    "A modern AI assistant that sheds new light on legal judgements through structured Q&A, predictive outcomes, and explainable reasoning."
)

# Upload judgment PDF
uploaded_pdf = st.file_uploader("Upload Judgement PDF", type=["pdf"])

if uploaded_pdf:
    st.info("Displaying the uploaded judgement PDF content:")
    display_pdf_content(uploaded_pdf)

    # Generate Q&A
    if st.button("Generate Q&A"):
        qa_json_path = r"C:\Users\nacha\Downloads\qa_pairs_sat_pal.json"
        qa_pairs = load_json_file(qa_json_path)
        if qa_pairs:
            st.session_state.qa_pairs = qa_pairs

# Display Q&A
if "qa_pairs" in st.session_state:
    qa_pairs = st.session_state.qa_pairs
    st.subheader("Generated Q&A Pairs")
    for idx, pair in enumerate(qa_pairs, start=1):
        question = pair.get("question", "").strip()
        answer = pair.get("answer", "").strip()
        st.markdown(f"**Q{idx}: {question}**")
        st.markdown(f"**A{idx}: {answer}**")
        st.write("---")

    # Download Q&A
    st.download_button(
        label="Download Q&A JSON",
        data=json.dumps(qa_pairs, indent=4, ensure_ascii=False),
        file_name="output_qa.json",
        mime="application/json"
    )

    # Generate prediction
    if st.button("Generate Judgement Predicted Label"):
        prediction_path = r"C:\Users\nacha\Downloads\sat_pal_prediction.json"
        predicted = load_json_file(prediction_path)
        if predicted:
            st.session_state.prediction_label = predicted

# Display prediction
if "prediction_label" in st.session_state:
    prediction = st.session_state.prediction_label[0]
    st.subheader("Judgement Prediction")
    st.markdown(f"**Case Name:** {prediction.get('case_name', '')}")
    st.markdown(f"**Judgement Date:** {prediction.get('judgement_date', '')}")
    st.markdown(f"**Predicted Label:** {prediction.get('predicted_label', '')}")

    # Download prediction
    st.download_button(
        label="Download Predicted Label JSON",
        data=json.dumps(st.session_state.prediction_label, indent=4, ensure_ascii=False),
        file_name="sat_pal_prediction.json",
        mime="application/json"
    )

    # Generate Explanation
    if st.button("Generate Explanation"):
        explanation_path = r"C:\Users\nacha\Downloads\sat_pal_explanation_flan.json"
        explanation = load_json_file(explanation_path)
        if explanation:
            st.session_state.explanation_data = explanation

# Display Explanation
if "explanation_data" in st.session_state:
    explanation = st.session_state.explanation_data[0]
    st.subheader("Explanation for Judgement Prediction")
    st.markdown(f"**Case Name:** {explanation.get('case_name', '')}")
    st.markdown(f"**Judgement Date:** {explanation.get('judgement_date', '')}")
    st.markdown(f"**Predicted Label:** {explanation.get('predicted_label', '')}")
    st.markdown(f"**Explanation:** {explanation.get('explanation', '')}")
    st.markdown(f"**Source:** {explanation.get('source', '')}")

    # Download explanation
    st.download_button(
        label="Download Explanation JSON",
        data=json.dumps(st.session_state.explanation_data, indent=4, ensure_ascii=False),
        file_name="sat_pal_explanation_flan.json",
        mime="application/json"
    )
