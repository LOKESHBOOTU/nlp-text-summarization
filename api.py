# ================================
# 📦 Imports
# ================================
from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import extractive_summarizer, abstractive_summarizer

# ================================
# 🚀 App Initialization
# ================================
app = FastAPI(
    title="NLP Text Summarization API",
    description="API for Extractive and Abstractive Text Summarization",
    version="1.0"
)

# ================================
# 📥 Request Schema
# ================================
class TextRequest(BaseModel):
    text: str
    sentences: int = 2


# ================================
# 🏠 Home Route
# ================================
@app.get("/")
def home():
    return {
        "message": "🚀 NLP Summarization API is running",
        "endpoint": "/summarize"
    }


# ================================
# 🧠 Summarization Endpoint
# ================================
@app.post("/summarize")
def summarize_text(request: TextRequest):

    # Validate input
    if not request.text or not request.text.strip():
        return {
            "extractive": "⚠️ No input text provided",
            "abstractive": "⚠️ No input text provided"
        }

    # Limit sentences
    sentences = max(1, min(6, request.sentences))

    # Extractive Summary
    try:
        ext_summary = extractive_summarizer(request.text, sentences)
    except Exception:
        ext_summary = "❌ Error in extractive summarization"

    # Abstractive Summary
    try:
        abs_summary = abstractive_summarizer(request.text)
    except Exception:
        abs_summary = "❌ Error in abstractive summarization"

    return {
        "extractive": ext_summary,
        "abstractive": abs_summary
    }


# ================================
# 🩺 Health Check Endpoint
# ================================
@app.get("/health")
def health_check():
    return {"status": "OK"}