# app.py  (updated)
import streamlit as st
import os
from ingest import save_uploaded_video, transcribe_audio
from chunking import chunk_transcript
from vectorstore import build_vectorstore, load_vectorstore
from rag_chain import build_rag_chain

st.title("Video RAG Chatbot")

# --- Sidebar: Video upload ---
with st.sidebar:
    st.header("Upload a Video")
    uploaded_file = st.file_uploader(
        "Choose a video file",
        type=["mp4", "mkv", "avi", "mov", "webm"]
    )

    if uploaded_file and st.button("Process Video"):
        with st.spinner("Saving video..."):
            tmp_path = save_uploaded_video(uploaded_file)

        with st.spinner("Transcribing with Whisper..."):
            transcript = transcribe_audio(tmp_path)

        with st.spinner("Chunking & building vector store..."):
            chunks = chunk_transcript(transcript)
            build_vectorstore(chunks)

        os.unlink(tmp_path)  # clean up temp file
        st.success(f"Done! '{uploaded_file.name}' is ready.")

# --- Main: Chat ---
if os.path.exists("./chroma_db"):
    vectordb = load_vectorstore()
    chain = build_rag_chain(vectordb)

    user_query = st.chat_input("Ask something about the video...")
    if user_query:
        with st.chat_message("user"):
            st.write(user_query)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chain.run(user_query)
                st.write(response)                
else:
    st.info("Upload a video in the sidebar to get started.")
