# RAG Chatbot

A video-to-chatbot application that transcribes videos, chunks the content, and answers questions about them using Retrieval-Augmented Generation (RAG).

## Features

- **Video Upload**: Support for MP4, MKV, AVI, MOV, WebM formats
- **Automatic Transcription**: Uses OpenAI's Whisper model for audio transcription
- **Vector Store**: ChromaDB for semantic search and retrieval
- **RAG Chain**: LLM-powered question answering based on video content
- **Interactive UI**: Streamlit-based web interface

## Tech Stack

- **Frontend**: Streamlit
- **Transcription**: OpenAI Whisper
- **Vector DB**: ChromaDB
- **LLM**: LangChain + LLM integration
- **Python 3.13**

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/saathvik999/RAG_CHATBOT.git
   cd RAG_CHATBOT
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv rag-env
   source rag-env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Activate the environment**:
   ```bash
   source rag-env/bin/activate
   ```

2. **Run the Streamlit app**:
   ```bash
   streamlit run rag-env/app.py
   ```

3. **Upload a video**:
   - Use the sidebar to upload a video file
   - The app will transcribe it, chunk the content, and build a vector store
   - Start asking questions about the video content!

## Project Structure

```
RAG_CHATBOT/
├── app.py              # Main Streamlit application
├── ingest.py           # Video ingestion and transcription
├── chunking.py         # Text chunking logic
├── vectorstore.py      # ChromaDB setup and management
├── rag_chain.py        # RAG chain implementation
├── requirements.txt    # Python dependencies
└── chroma_db/          # Vector store database (generated)
```

## Requirements

- Python 3.10+
- FFmpeg (for audio extraction from videos)
- 4GB+ RAM (for Whisper model)

## Environment Variables

Create a `.env` file if needed for LLM API keys:
```
OPENAI_API_KEY=your_key_here
```

## Troubleshooting

- **"Whisper model not found"**: First run will download the base model (~140MB)
- **"ffmpeg not found"**: Install FFmpeg via Homebrew: `brew install ffmpeg`
- **Vector store not loading**: Ensure `chroma_db/` directory exists from a previous video upload

## Future Enhancements

- [ ] Support for PDFs, documents, and web content
- [ ] Multiple video processing
- [ ] Fine-tuned models for domain-specific Q&A
- [ ] Export chat history
- [ ] Deployment to cloud (Hugging Face Spaces, etc.)

## License

MIT

## Author

Saathvik
