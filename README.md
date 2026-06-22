# SugarCoat.ai

Proyek ini terdiri dari dua area utama:

- `Deployment` — sumber daya untuk menjalankan model sebagai layanan API.
- `Modeling` — data dan artefak pelatihan untuk membangun model.

## Folder Deployment

Folder `Deployment` berisi semua file yang diperlukan untuk menjalankan model SugarCoat.ai sebagai API FastAPI.

Konten utama:

- `Dockerfile` — konfigurasi image Docker yang menggunakan `python:3.10-slim`.
- `main.py` — aplikasi FastAPI yang memuat `sugarcoat_model.keras` dan menyediakan endpoint `/predict`.
- `requirements.txt` — paket Python yang diperlukan untuk menjalankan server.
- `sugarcoat_model.keras` — model TensorFlow hasil pelatihan.

Tujuan folder ini:

- Menyediakan environment deployment yang siap dipakai.
- Mendukung deployment di Hugging Face Spaces dengan hanya mengunggah file yang ada.
- Menyediakan endpoint API untuk inferensi risiko gaya hidup.

Link deployment yang sudah tersedia:

- Aplikasi FastAPI: https://Ifanhakm-sugarcoat-api.hf.space
- Dokumentasi OpenAPI: https://Ifanhakm-sugarcoat-api.hf.space/docs
- Endpoint inferensi: https://Ifanhakm-sugarcoat-api.hf.space/predict

## Folder Modeling

Folder `Modeling` berisi dataset dan log pelatihan model.

Isi folder `Modeling`:

- `dataset_sugarcoat.csv` — dataset yang dipakai untuk membangun model prediksi.
- `[Modelling] SugarCoat_ai.ipynb` — notebook untuk eksplorasi data, pelatihan, dan analisis model.
- `logs/fit/` — direktori log TensorBoard yang berisi informasi pelatihan dan validasi.

Tujuan folder ini:

- Menyimpan data mentah yang digunakan untuk analisis dan pelatihan.
- Menyimpan hasil eksperimen training agar alur pelatihan bisa ditinjau kembali.

## Ringkasan alur kerja

1. Data dan eksperimen model berada di folder `Modeling`.
2. Setelah model siap, artefak `sugarcoat_model.keras` dapat dibawa ke folder `Deployment`.
3. Folder `Deployment` selanjutnya menjadi basis untuk menjalankan aplikasi API, baik lokal maupun di Hugging Face Spaces.
