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

A simple NLP-based text summarization project with:

- a `FastAPI` backend for extractive and abstractive summarization
- a `Gradio` frontend for entering text or uploading a PDF
- PDF export for the generated abstractive summary

## Features

- Extractive summarization
- Abstractive summarization using `transformers`
- PDF text extraction with `PyPDF2`
- Download summary as PDF
- Local development support in VS Code

## Project Structure

```text
Text summarization/
|-- api.py
|-- app.py
|-- summarizer.py
|-- requirements.txt
|-- Dockerfile
|-- README.md
`-- .vscode/
```

## Live Demo

Live demo URL:

- [https://huggingface.co/spaces/Lokeshbootu/nlp-text-summarizer](https://huggingface.co/spaces/Lokeshbootu/nlp-text-summarizer)

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

## Requirements

- Python 3.10 or later recommended
- VS Code
- A virtual environment in `venv`

## Installation

Open the project folder in VS Code, then run:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If the virtual environment does not exist yet, create it first:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run in VS Code

This project is already configured with:

- [launch.json](C:\Users\LOKESHBOOTU\OneDrive\Desktop\Text summarization\.vscode\launch.json)
- [settings.json](C:\Users\LOKESHBOOTU\OneDrive\Desktop\Text summarization\.vscode\settings.json)

### Option 1: Run from the VS Code Run Button

1. Open the folder in VS Code.
2. Open the `Run and Debug` panel.
3. Select `Run API + UI`.
4. Click the green Run button.

This starts:

- FastAPI backend at [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Gradio frontend at [http://127.0.0.1:7860](http://127.0.0.1:7860)

### Option 2: Run Manually in Two Terminals

Terminal 1:

```powershell
.\venv\Scripts\Activate.ps1
uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

Terminal 2:

```powershell
.\venv\Scripts\Activate.ps1
python app.py
```

## API Endpoints

- `GET /` - home route
- `GET /health` - health check
- `POST /summarize` - returns extractive and abstractive summaries

API docs:

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## How to Use

1. Start the backend and frontend.
2. Open the Gradio UI in your browser.
3. Enter text or upload a PDF.
4. Choose the number of extractive sentences.
5. Click `Generate Summary`.
6. View the extractive and abstractive summaries.
7. Download the summary as a PDF.

## Notes

- The frontend reads the backend URL from the `API_URL` environment variable.
- For local development, the default backend URL is `http://127.0.0.1:8000/summarize`.
- The first run may take time because the summarization model may need to load.
- `nltk` resources such as `punkt` and `stopwords` are downloaded automatically on startup.

## Docker

You can also run the project with Docker.

Build:

```powershell
docker build -t text-summarizer .
```

Run:

```powershell
docker run -p 7860:7860 -p 8000:8000 text-summarizer
```

## Deploy to Hugging Face Spaces

This repository is prepared for a `Docker` Space.

### Steps

1. Create a new Space on Hugging Face.
2. Choose `Docker` as the Space SDK.
3. Name it something like `nlp-text-summarizer`.
4. Upload or push the files from this repository.
5. Wait for the build to finish.
6. Open the generated public Space URL.

### Expected public URL

- `https://huggingface.co/spaces/<your-username>/nlp-text-summarizer`

### Notes for deployment

- The `README.md` already includes the Hugging Face Spaces YAML config block.
- The app is exposed on port `7860`, which Hugging Face uses as the public app port.
- The FastAPI backend runs internally on port `8000` inside the same container.
- The summarization model may take time to download during the first build or first run.

## Troubleshooting

### `ModuleNotFoundError` or missing package errors

Run:

```powershell
pip install -r requirements.txt
```

### Frontend shows `API not running`

Make sure the FastAPI server is running on port `8000`.

### VS Code does not detect the interpreter

Open Command Palette and choose:

```text
Python: Select Interpreter
```

Then select:

```text
venv\Scripts\python.exe
```

## Author

Update this section with your name, GitHub profile, or portfolio link.
