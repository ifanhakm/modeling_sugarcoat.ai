# Deployment

Berisi konfigurasi dan kode untuk menjalankan model SugarCoat.ai sebagai layanan API menggunakan FastAPI dan Docker.

Folder ini juga disiapkan agar dapat diunggah ke Hugging Face Spaces sebagai deployment API, selama file `sugarcoat_model.keras` dan dependensi tersedia.

## Link Deployment

- **Aplikasi FastAPI**: https://Ifanhakm-sugarcoat-api.hf.space
- **Dokumentasi OpenAPI**: https://Ifanhakm-sugarcoat-api.hf.space/docs
- **Endpoint inferensi**: https://Ifanhakm-sugarcoat-api.hf.space/predict

## Struktur folder

- `Dockerfile` - definisi image Docker untuk build container.
- `main.py` - aplikasi FastAPI yang memuat model `sugarcoat_model.keras` dan menyediakan endpoint `/predict`.
- `requirements.txt` - daftar paket Python yang diperlukan.
- `sugarcoat_model.keras` - model TensorFlow untuk inferensi.

## Cara kerja

1. Docker build menggunakan image `python:3.10-slim`.
2. Dependensi diinstal dari `requirements.txt`.
3. Semua file dalam folder `Deployment` disalin ke dalam image.
4. Ketika container berjalan, `uvicorn` menjalankan `main:app` pada host `0.0.0.0` port `7860`.
5. Endpoint utama:
   - `GET /` - mengecek apakah API aktif.
   - `POST /predict` - menerima payload dan mengembalikan prediksi risiko.

## Request `POST /predict`

Gunakan JSON dengan key berikut:

- `age` (int)
- `gender` (str): `Female` atau `Male`
- `employment_status` (str): `Employed`, `Retired`, `Student`, atau `Unemployed`
- `smoking_status` (str): `Current`, `Former`, atau `Never`
- `alcohol_consumption_per_week` (int)
- `physical_activity_minutes_per_week` (int)
- `sleep_hours_per_day` (float)
- `screen_time_hours_per_day` (float)
- `family_history_diabetes` (int)
- `hypertension_history` (int)
- `cardiovascular_history` (int)
- `bmi` (float)
- `sweet_beverages_per_week` (int)

Contoh request:

```json
{
  "age": 22,
  "gender": "Male",
  "employment_status": "Student",
  "smoking_status": "Never",
  "alcohol_consumption_per_week": 2,
  "physical_activity_minutes_per_week": 120,
  "sleep_hours_per_day": 7.0,
  "screen_time_hours_per_day": 5.5,
  "family_history_diabetes": 0,
  "hypertension_history": 0,
  "cardiovascular_history": 0,
  "bmi": 22.8,
  "sweet_beverages_per_week": 3
}
```

Respons JSON contoh:

```json
{
  "status": "success",
  "is_risky": false,
  "probability": 0.1234,
  "roast_trigger": "HEALTHY"
}
```

## Deployment di Hugging Face Spaces

Unggah isi folder `Deployment` ke Hugging Face Spaces:
- `Dockerfile`
- `main.py`
- `requirements.txt`
- `sugarcoat_model.keras`

maka Spaces akan membangun dan menjalankan aplikasi secara otomatis. Tidak perlu menjalankan `docker build` atau `uvicorn` sendiri jika sudah memakai Spaces.

## Build & run Docker (opsional)

Untuk pengujian lokal tanpa Spaces, dari folder `Deployment` jalankan:

```bash
docker build -t sugarcoat-api .
docker run --rm -p 7860:7860 sugarcoat-api
```

## Run lokal tanpa Docker (opsional)

Pastikan Python 3.10+ sudah terpasang, lalu:

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 7860
```

> Pastikan file `sugarcoat_model.keras` ada di folder `Deployment` sebelum menjalankan server.

## Catatan penting

- `main.py` hanya mendefinisikan objek FastAPI `app`; server dijalankan oleh `uvicorn`.
- Jika `sugarcoat_model.keras` tidak ditemukan, aplikasi akan gagal saat startup.
- Mapping input teks ke angka ditangani secara internal di `main.py`.

## Dependensi utama

- `fastapi`
- `uvicorn`
- `pydantic`
- `pandas`
- `numpy`
- `tensorflow-cpu`
- `tensorflow-recommenders`
