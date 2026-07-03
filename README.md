# 🤖 AI Resume-Based Interview Coach

An AI-powered interview preparation application that analyzes a candidate's resume, extracts technical skills, retrieves relevant interview questions using Retrieval-Augmented Generation (RAG), generates personalized interview questions, and evaluates candidate responses using the Ollama Llama 3 Large Language Model.

---

## 📌 Project Overview

Traditional interview preparation platforms ask the same questions to every candidate regardless of their background.

This project provides a personalized interview experience by analyzing the candidate's resume and generating skill-based interview questions using AI and RAG.

---

## ✨ Features

- 📄 Upload Resume (PDF)
- 📝 Extract Resume Text
- 🔍 Detect Technical Skills Automatically
- 📚 Upload Interview Question Bank (PDF)
- 🧠 Build a RAG Pipeline using ChromaDB
- 🤖 Generate Personalized Interview Questions using Ollama (Llama 3)
- 💬 Candidate Answer Submission
- 📊 AI-Based Answer Evaluation
- ⭐ Technical Score
- 🗣️ Communication Score
- 💪 Confidence Score
- ✅ Strengths & Weaknesses
- 📖 Missing Concepts
- 💡 Suggestions for Improvement
- 🎯 Final Recommendation

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Ollama (Llama 3)
- ChromaDB
- PyPDF2
- Sentence Transformers
- Retrieval-Augmented Generation (RAG)

---

## 📂 Project Structure

```
AI_Resume_Interview_Coach
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── utils
│   ├── pdf_reader.py
│   ├── skill_extractor.py
│   ├── rag.py
│   ├── question_generator.py
│   └── evaluator.py
│
├── resume
├── interview_questions
└── chroma_db
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Interview-Coach.git

cd AI-Resume-Interview-Coach
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Ollama

Download and install Ollama from:

https://ollama.com/download

Run the model:

```bash
ollama run llama3
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

1. Upload Resume
2. Extract Resume Text
3. Extract Technical Skills
4. Upload Interview Question PDF
5. Build ChromaDB Vector Database
6. Retrieve Relevant Questions using RAG
7. Generate Personalized Interview Question
8. Candidate Answers the Question
9. AI Evaluates the Answer
10. Display Scores and Feedback

---

## 📊 AI Evaluation

The application provides:

- Technical Score (/10)
- Communication Score (/10)
- Confidence Score (/10)
- Strengths
- Weaknesses
- Missing Concepts
- Correct Answer
- Suggestions for Improvement
- Final Recommendation

---

## 🎯 Future Enhancements

- Voice-based Interview
- User Authentication
- Interview History
- PDF Report Generation
- Performance Dashboard
- Cloud Deployment

---

## 👩‍💻 Author

**Pothula Bhargavi Venkata Naga Sai**

B.Tech - Information Technology

Swarnandhra College of Engineering and Technology

---

## 🙏 Acknowledgements

This project was developed as part of the **Generative AI with Prompt Engineering Workshop** to demonstrate the practical application of Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and AI-powered interview assistance.
