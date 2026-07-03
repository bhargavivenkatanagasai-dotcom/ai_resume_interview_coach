
        import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.rag import create_vector_database, retrieve_questions
from utils.question_generator import generate_interview_question
from utils.evaluator import evaluate_answer

st.set_page_config(
    page_title="AI Resume-Based Interview Coach",
    layout="wide"
)

# Session State
if "question" not in st.session_state:
    st.session_state.question = ""

if "question_no" not in st.session_state:
    st.session_state.question_no = 1

if "evaluated" not in st.session_state:
    st.session_state.evaluated = False

st.title("AI Resume-Based Interview Coach")

st.write("Upload your Resume and Interview Question PDF")

# Resume Upload

resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if resume_file is not None:

    st.success("Resume Uploaded Successfully")

    resume_text = extract_text_from_pdf(resume_file)

    st.subheader("Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=250
    )

    skills = extract_skills(resume_text)

    st.subheader("Extracted Skills")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No skills found.")

    st.divider()

    interview_pdf = st.file_uploader(
        "Upload Interview Question PDF",
        type=["pdf"],
        key="questions"
    )

    if interview_pdf is not None:

        st.success("Interview Question PDF Uploaded")

        interview_text = extract_text_from_pdf(interview_pdf)

        db = create_vector_database(interview_text)

        docs = retrieve_questions(db, skills)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        st.success("RAG Database Created")

        # Generate first question only once
        if st.session_state.question == "":
            st.session_state.question = generate_interview_question(
                skills,
                context
            )

        st.subheader(
            f"Interview Question {st.session_state.question_no}"
        )

        st.info(st.session_state.question)

        answer = st.text_area(
            "Type Your Answer",
            key=f"answer_{st.session_state.question_no}"
        )

        if st.button("Evaluate Answer"):

            if answer.strip() == "":
                st.warning("Please enter your answer.")

            else:

                with st.spinner("AI is evaluating your answer..."):

                    result = evaluate_answer(
                        st.session_state.question,
                        answer
                    )

                st.subheader("AI Evaluation")

                st.write(result)

                st.session_state.evaluated = True

        if st.session_state.evaluated:

            if st.button("Next Question"):

                docs = retrieve_questions(db, skills)

                context = "\n\n".join(
                    [doc.page_content for doc in docs]
                )

                st.session_state.question = generate_interview_question(
                    skills,
                    context
                )

                st.session_state.question_no += 1
                st.session_state.evaluated = False

                st.rerun()
