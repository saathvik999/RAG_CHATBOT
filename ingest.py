# ingest.py  (updated)
import whisper
import tempfile
import os

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

def save_uploaded_video(uploaded_file):
    """Save Streamlit UploadedFile to a temp file and return its path."""
    suffix = os.path.splitext(uploaded_file.name)[-1]  # e.g. .mp4, .mkv
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        return tmp.name