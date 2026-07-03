from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

def evaluate_answer(question, answer):

    prompt = f"""
You are an expert technical interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and provide:

Technical Score (/10)
Communication Score (/10)
Confidence Score (/10)

Strengths

Weaknesses

Missing Concepts

Correct Answer

Suggestions for Improvement

Final Recommendation
"""

    response = llm.invoke(prompt)

    return response.content