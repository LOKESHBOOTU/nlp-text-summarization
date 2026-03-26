# ================================
# 📦 Imports
# ================================
import nltk
import re
import time
from string import punctuation
from heapq import nlargest
import torch
from transformers import pipeline

# ================================
# 📥 NLTK Setup
# ================================
try:
    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)
except Exception:
    # Offline or restricted environments should still be able to boot.
    pass

# ================================
# 🔤 Tokenizers (Fallback Safe)
# ================================
def simple_sentence_tokenize(text):
    return re.split(r'(?<=[.!?])\s+', text.strip())

def simple_word_tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# ================================
# 🧹 Stopwords
# ================================
try:
    STOP_WORDS = set(nltk.corpus.stopwords.words("english")) | set(punctuation)
except:
    STOP_WORDS = set(punctuation)

# ================================
# 🤖 Load Model (ONLY ONCE)
# ================================
MODEL_NAME = "sshleifer/distilbart-cnn-6-6"
DEVICE = 0 if torch.cuda.is_available() else -1

print(f"Using {'GPU' if DEVICE == 0 else 'CPU'}")

summarizer = None
try:
    summarizer = pipeline("summarization", model=MODEL_NAME, device=DEVICE)
    print("Model loaded successfully")
except Exception:
    print("Model failed, fallback will be used")
    summarizer = None

# ================================
# ✂️ Extractive Summarizer
# ================================
from nltk.tokenize import sent_tokenize, word_tokenize

def extractive_summarizer(text, sentence_count=2):

    if not text or not text.strip():
        return ""

    try:
        sentences = sent_tokenize(text)
    except:
        sentences = simple_sentence_tokenize(text)

    sentence_count = max(1, min(6, int(sentence_count)))

    if len(sentences) <= sentence_count:
        return " ".join(sentences)

    try:
        words = word_tokenize(text.lower())
    except:
        words = simple_word_tokenize(text)

    freq = {}
    for word in words:
        if word.isalnum() and word not in STOP_WORDS:
            freq[word] = freq.get(word, 0) + 1

    sentence_scores = {}
    for sent in sentences:
        try:
            tokens = word_tokenize(sent.lower())
        except:
            tokens = simple_word_tokenize(sent)

        score = sum(freq.get(w, 0) for w in tokens)
        if score > 0:
            sentence_scores[sent] = score

    if not sentence_scores:
        return " ".join(sentences[:sentence_count])

    best_sentences = nlargest(sentence_count, sentence_scores, key=sentence_scores.get)

    # Preserve original order
    ordered = [s for s in sentences if s in best_sentences]

    return " ".join(ordered)

# ================================
# 📦 Chunking (for long text)
# ================================
def chunk_text(text, max_chars=800):

    try:
        sentences = sent_tokenize(text)
    except:
        sentences = simple_sentence_tokenize(text)

    chunks = []
    current = ""

    for s in sentences:
        if len(current) + len(s) < max_chars:
            current += " " + s
        else:
            chunks.append(current.strip())
            current = s

    if current:
        chunks.append(current.strip())

    return chunks

# ================================
# 🧠 Abstractive Summarizer
# ================================
def abstractive_summarizer(text):

    if not text or not text.strip():
        return ""

    # If model failed → fallback
    if summarizer is None:
        return extractive_summarizer(text, sentence_count=2)

    # Short text
    try:
        if len(text) < 1000:
            output = summarizer(
                text,
                max_length=120,
                min_length=30,
                do_sample=False
            )
            return output[0]['summary_text']
    except:
        return extractive_summarizer(text, 2)

    # Long text → chunking
    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:
        try:
            result = summarizer(
                chunk,
                max_length=120,
                min_length=30,
                do_sample=False
            )
            summaries.append(result[0]['summary_text'])
        except:
            summaries.append(extractive_summarizer(chunk, 1))

        time.sleep(0.02)

    combined = " ".join(summaries)

    # Final summary
    try:
        final = summarizer(
            combined,
            max_length=120,
            min_length=30,
            do_sample=False
        )
        return final[0]['summary_text']
    except:
        return combined
