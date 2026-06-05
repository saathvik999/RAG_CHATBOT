# rag_chain.py
from langchain_community.llms import Ollama
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

def build_rag_chain(vectordb):
    llm = Ollama(model="deepseek-r1:8b")
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are a helpful assistant. Use the following video transcript context to answer the question.

Context: {context}

Question: {question}

Answer clearly and cite specific parts of the video when relevant."""
    )
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )
    return chain