"""Initial Streamlit landing page for Resume Skill Gap Analyzer.

The application is a scaffold. It deliberately does not claim that planned
modelling, evaluation, or deployment features are implemented.
"""
import streamlit as st

st.set_page_config(page_title="Resume Skill Gap Analyzer", page_icon="🧪", layout="wide")
st.title("Resume Skill Gap Analyzer")
st.caption("Explainable resume–job alignment using natural language processing")
st.warning("Development scaffold: core workflows are being implemented.")

st.subheader("Research question")
st.write("How can a system identify meaningful skill alignment while distinguishing explicitly evidenced skills, related experience, and skills that are not evidenced in the supplied resume?")

st.subheader("Planned methodology")
for item in ["Resume and job-description text extraction", "Structured skill identification with supporting text spans", "Keyword matching baseline", "TF-IDF and cosine-similarity baseline", "Sentence Transformer semantic similarity", "Evidence-based categories: supported, related, and not evidenced", "Role-specific skill-gap summary and learning suggestions"]:
    st.write("• " + item)

st.subheader("Project status")
st.write("Scope defined · Implementation in progress · Evaluation pending · Deployment pending")
