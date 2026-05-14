import streamlit as st
import joblib

from utils.parser import extract_text_from_pdf
from utils.preprocess import clean_text

# Load model and vectorizer
model = joblib.load('model.pkl')
tfidf = joblib.load('tfidf.pkl')

# Streamlit page config
st.set_page_config(page_title="AI Resume Screening System")

st.title("AI Resume Screening System")

st.write("Upload Resume PDF")

uploaded_file = st.file_uploader("Choose PDF Resume", type=['pdf'])

job_description = st.text_area("Paste Job Description")

if uploaded_file is not None:

    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.write(resume_text[:1000])

    # Clean text
    cleaned_resume = clean_text(resume_text)

    # Transform using TF-IDF
    resume_vector = tfidf.transform([cleaned_resume])

    # Predict category
    prediction = model.predict(resume_vector)[0]

    st.subheader("Predicted Job Category")
    st.success(prediction)

    # Job description matching
    if job_description:

        cleaned_jd = clean_text(job_description)

        jd_vector = tfidf.transform([cleaned_jd])

        from sklearn.metrics.pairwise import cosine_similarity

        similarity = cosine_similarity(resume_vector, jd_vector)

        match_score = round(similarity[0][0] * 100, 2)

        st.subheader("Resume Match Score")
        st.info(f"{match_score}% Match")

  streamlit run app.py
