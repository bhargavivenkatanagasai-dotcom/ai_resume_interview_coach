from langchain_ollama import ChatOllama

# Load Llama 3
llm = ChatOllama(model="llama3")

def generate_interview_question(skills, context):

    prompt = f"""
You are an experienced technical interviewer.

Candidate Skills:
{skills}

Reference Questions:
{context}

Generate ONE personalized interview question based on the candidate's skills.

Return only the interview question.
"""

    response = llm.invoke(prompt)

    return response.content