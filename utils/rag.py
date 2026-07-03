from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def create_vector_database(text):

    # Split the interview question PDF into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    # Create embeddings
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Store in ChromaDB
    db = Chroma.from_texts(
        texts=chunks,
        embedding=embedding,
        persist_directory="chroma_db"
    )

    return db


def retrieve_questions(db, skills):

    query = " ".join(skills)

    docs = db.similarity_search(
        query,
        k=5
    )

    return docs