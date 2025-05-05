# Emotion Detection from Text using NLP

This project demonstrates a simple text emotion detection system using NLP and a pre-trained transformer model.

## 💡 Features
- Uses Hugging Face `distilbert-base-uncased-emotion` model
- Simple web interface using Streamlit
- Modified dataset includes `neutral` class
- Interactive demo for real-time emotion prediction

## 🚀 How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/kiyoll/emotion-detection-nlp.git
cd emotion-detection-nlp
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app:**
```bash
streamlit run app.py
```

## 📦 Dependencies

- transformers
- streamlit

## 🔍 Example

Input:
> I’m feeling wonderful today!

Output:
> 🎯 Emosi Terdeteksi: `joy`  
> Confidence Score: `0.95`

## 📁 Dataset

Dataset used: `data.csv` with emotion labels like:
- joy
- sadness
- anger
- love
- **neutral** (added manually)

## 📜 License

MIT
