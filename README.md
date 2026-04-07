# ✨ AI StoryCraft – Multimodal AI Image-to-Story Generator

## 📌 Overview

This project is a Multimodal AI application that converts an input image into a descriptive scenario, generates a creative story, and produces audio narration.

The system integrates Computer Vision, Natural Language Processing, and Speech Synthesis using modern AI tools.

---

## 🚀 Features

* 📷 Image to text (BLIP model)
* 📖 Story generation (LLM via Ollama)
* 🔊 Audio narration (gTTS)
* 🎨 Interactive UI (Streamlit)

---

## 🧠 Tech Stack

* Python
* Hugging Face Transformers (BLIP)
* Ollama (Phi Model)
* LangChain
* Streamlit
* gTTS

---

## 🔄 Workflow

Image → Caption → Story → Audio → Display

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Nupur-07/AI-StoryCraft
cd AI
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install streamlit transformers torch torchvision langchain langchain-community python-dotenv gtts pillow
```

### 4. Run Ollama Model

```bash
ollama run phi
```

### 5. Run Application

```bash
streamlit run app.py
```

---

## 📸 Output

* Generated Image Caption
* AI Generated Story
* Audio Narration

---

## 🎯 Future Improvements

* Multi-language support
* Emotion-based voice
* Advanced UI design
* Cloud deployment

---

## 👩‍💻 Author

Nupur
