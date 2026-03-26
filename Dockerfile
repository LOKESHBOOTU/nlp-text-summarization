# Use lightweight Python image
FROM python:3.10-slim

# Create a non-root user for Hugging Face Spaces compatibility
RUN useradd -m -u 1000 user
USER user

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Set working directory
WORKDIR $HOME/app

# Copy all files
COPY --chown=user . $HOME/app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Set port (HF uses this)
ENV PORT=7860

# Expose ports
EXPOSE 7860
EXPOSE 8000

# Run API + UI together
CMD ["sh", "-c", "uvicorn api:app --host 127.0.0.1 --port 8000 & python app.py"]
