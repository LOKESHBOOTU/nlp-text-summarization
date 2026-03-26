---
title: NLP Text Summarizer
emoji: 📄
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
short_description: Upload a PDF or paste text to generate extractive and abstractive summaries.
---

# NLP Text Summarizer

A Python, FastAPI, and Gradio based project for generating extractive and abstractive summaries from plain text or PDF documents. The system allows users to paste text, upload a PDF, choose the number of extractive sentences, and download the final summary as a PDF file.

## What Is NLP Text Summarization

NLP text summarization is the process of reducing a large piece of text into a shorter version while preserving the main meaning and important information. It is a Natural Language Processing task used to help readers understand lengthy content quickly and efficiently.

This project supports two common approaches:

- Extractive summarization, which selects the most important sentences from the original text
- Abstractive summarization, which generates a shorter summary in a more natural rewritten form

## Live Demo

[Click here for Live Demo](https://huggingface.co/spaces/Lokeshbootu/nlp-text-summarizer)

## How It Works

1. Enter text manually or upload a PDF file.
2. Choose the number of extractive summary sentences.
3. Click `Generate Summary`.
4. View both extractive and abstractive summaries.
5. Download the generated summary as a PDF.

## Sample Preview

<img width="1757" height="981" alt="image" src="https://github.com/user-attachments/assets/19aae778-3a4e-4b5d-ac9b-a4c940defa3a" />

Example sections to include:

- Main interface with text input and PDF upload
- Output preview showing extractive summary, abstractive summary, and download option

## Features

- Extractive text summarization
- Abstractive text summarization using Transformers
- PDF upload and text extraction
- Download summary as PDF
- FastAPI backend for summarization
- Gradio based interactive interface

## Applications

- Summarizing news articles
- Generating short notes from research papers
- Reducing long reports into quick overviews
- Summarizing educational content for students
- Creating concise summaries from business documents
- Extracting key points from uploaded PDF files

## Why This Project Is Useful

- Saves time when reading long content
- Helps users focus on key information
- Improves productivity for students, researchers, and professionals
- Makes document review simpler and faster

## Project Structure

```text
Text summarization/
|-- api.py
|-- app.py
|-- summarizer.py
|-- requirements.txt
|-- Dockerfile
|-- README.md
|-- .gitignore
`-- .vscode/
```

## Requirements

- Python 3.10 or later
- pip

## Installation

```bash
pip install -r requirements.txt
```

If you do not have a virtual environment yet, create one first:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run Locally

Run the backend in one terminal:

```bash
uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

Run the frontend in another terminal:

```bash
python app.py
```

Then open the app in your browser:

[http://127.0.0.1:7860](http://127.0.0.1:7860)

## API Endpoints

- `GET /`
- `GET /health`
- `POST /summarize`

API docs:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Input Options

You can use either of the following:

- Plain text entered into the text box
- PDF document upload

## Types of Summarization Used

### Extractive Summarization

Extractive summarization identifies the most relevant sentences from the original text and combines them into a shorter summary without changing the wording much.

### Abstractive Summarization

Abstractive summarization uses a language model to generate a new, shorter version of the text that captures the core meaning in a more human-like way.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Gradio
- Transformers
- Torch
- NLTK
- PyPDF2
- ReportLab

## Deployment

This project is configured for deployment on Hugging Face Spaces using Docker.

## Future Scope

- Support for more file formats such as DOCX and TXT
- Multi-language summarization
- User selectable summary length presets
- Better handling of very large documents
- Improved model performance with advanced transformer models
- Keyword extraction and topic detection
- User authentication and saved summary history
- Speech to text summarization for audio inputs

## Limitations

- Abstractive summary quality depends on the underlying model
- Very large documents may take more time to process
- The first run may be slower because the model needs to load
- Internet restrictions may affect model or NLTK resource downloads in some environments

## Conclusion

This project demonstrates how NLP can be used to make long text content easier to understand and faster to review. By combining extractive and abstractive approaches with a simple web interface, it provides a practical and user-friendly text summarization solution.

## Notes

- Do not upload `venv/`
- Do not upload `__pycache__/`
- Do not upload `.vscode/`
- Install dependencies from `requirements.txt` after cloning the repository
- The first run may take longer because the summarization model may need to load
