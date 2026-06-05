# vectorstore.py

import chromadb
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def build_vectorstore(chunks):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"  # saves to disk
    )
    vectordb.persist()
    return vectordb

def load_vectorstore():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )