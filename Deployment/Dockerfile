# image Python ringan
FROM python:3.10-slim

# Buat user baru
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Direktori kerja
WORKDIR /app

# Copy requirement dan install
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy file lainnya
COPY --chown=user . .

# Ekspos port default Hugging Face
EXPOSE 7860

# Menjalankan server FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]