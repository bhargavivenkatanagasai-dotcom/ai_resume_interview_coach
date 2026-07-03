def extract_skills(text):

    skills = [
        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "TensorFlow",
        "PyTorch",
        "LangChain",
        "RAG",
        "OpenAI",
        "Git",
        "GitHub",
        "HTML",
        "CSS",
        "JavaScript",
        "Streamlit"
    ]

    found = []

    text = text.lower()

    for skill in skills:
        if skill.lower() in text:
            found.append(skill)

    return found