# ================================
# 📦 Imports
# ================================
import gradio as gr
import requests
import os
from PyPDF2 import PdfReader
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Use localhost for local development in VS Code.
API_URL = os.environ.get("API_URL", "http://127.0.0.1:8000/summarize")

# ================================
# 📄 Extract text from PDF
# ================================
def extract_text_from_pdf(file):
    if file is None:
        return ""

    reader = PdfReader(file.name)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


# ================================
# 📥 Create PDF for download
# ================================
def create_pdf(summary_text):
    file_path = "summary_output.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph(summary_text, styles["Normal"]))

    doc.build(content)

    return file_path


# ================================
# 🎯 Main Function
# ================================
def generate_summary(text, pdf_file, sentences):

    # If PDF uploaded → override text
    if pdf_file is not None:
        text = extract_text_from_pdf(pdf_file)

    if not text or not text.strip():
        return "⚠️ No input provided", "⚠️ No input provided", None

    try:
        response = requests.post(
            API_URL,
            json={"text": text, "sentences": int(sentences)}
        )

        result = response.json()

        ext = result.get("extractive", "")
        abs_sum = result.get("abstractive", "")

        pdf_path = create_pdf(abs_sum)

        return ext, abs_sum, pdf_path

    except Exception:
        return "❌ API not running", "❌ API not running", None


# ================================
# 🎨 UI
# ================================
with gr.Blocks(title="NLP Text Summarizer") as demo:

    gr.Markdown("""
    # 🧠 NLP Text Summarizer
    ### Upload PDF or Enter Text → Get Summary → Download as PDF
    """)

    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(lines=10, label="✏️ Enter Text")

            pdf_input = gr.File(label="📄 Upload PDF", file_types=[".pdf"])

            sentence_slider = gr.Slider(1, 6, value=2, label="Extractive Sentences")

            btn = gr.Button("🚀 Generate Summary")

        with gr.Column():
            ext_output = gr.Textbox(label="📝 Extractive Summary")
            abs_output = gr.Textbox(label="🤖 Abstractive Summary")
            download_file = gr.File(label="📥 Download Summary as PDF")

    btn.click(
        fn=generate_summary,
        inputs=[text_input, pdf_input, sentence_slider],
        outputs=[ext_output, abs_output, download_file]
    )

# ================================
# 🚀 Launch
# ================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    demo.launch(
        server_name="0.0.0.0",
        server_port=port
    )
