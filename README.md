# ⚖️ LexNova

**LexNova** is a modern, AI-powered legal assistant that helps users explore court judgments with clarity and precision. It extracts structured Q&A from legal documents, predicts likely case outcomes, and provides explainable reasoning — all within an elegant and interactive interface.

---

##  Features

-  **Upload Legal Judgments (PDF)**  
  Upload court case files in PDF format for instant processing.

-  **Structured Q&A Extraction**  
  Automatically generates meaningful question-answer pairs from the document using text analysis.

-  **Outcome Prediction**  
  Uses AI models to predict the likely outcome of the case.

-  **Explainable AI (XAI) Reasoning**  
  Understand *why* a prediction was made with contextual legal explanations.

-  **Download Results**  
  Export generated Q&A, predictions, and explanations as JSON files.

---

##  Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – for the user interface
- [pdfplumber](https://github.com/jsvine/pdfplumber) – for PDF parsing
- JSON – for structured output data
- AI/ML integration for prediction and explanation (local or API-based)

---

##  Project Structure

```

LexNova/
├── app.py                 # Streamlit application
├── README.md              # Documentation
├── requirements.txt       # Dependencies (optional)

````

---

##  Getting Started

###  Prerequisites

- Python 3.7 or higher
- Install the required packages:

```bash
pip install streamlit pdfplumber
````

###  Run the App

```bash
streamlit run app.py
```

---

##  How It Works

1. **Upload** a legal judgment PDF.
2. Click **"Generate Q\&A"** to extract question-answer pairs from the text.
3. Click **"Generate Judgment Predicted Label"** to let the AI classify the outcome.
4. Click **"Generate Explanation"** to get a human-readable explanation of the AI's reasoning.
5. Use the **download buttons** to export any of the results as JSON files.

---

