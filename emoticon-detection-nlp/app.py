import streamlit as st
from transformers import pipeline

# Judul halaman
st.title("🧠 Deteksi Emosi dari Teks")

# Load model pipeline
@st.cache_resource
def load_model():
    return pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

emotion_classifier = load_model()

# Input dari pengguna
user_input = st.text_area("Masukkan kalimat (dalam Bahasa Inggris):", height=100)

if user_input:
    with st.spinner("Menganalisis emosi..."):
        result = emotion_classifier(user_input)[0]
        st.markdown(f"### 🎯 Emosi Terdeteksi: `{result['label']}`")
        st.write(f"Confidence Score: `{result['score']:.2f}`")
