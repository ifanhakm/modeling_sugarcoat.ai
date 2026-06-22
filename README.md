# SugarCoat.ai: Machine Learning Pipeline & API Deployment

This repository houses the core Machine Learning architecture and the production-ready API deployment for **SugarCoat.ai**, a preventative health assistant that utilizes a Deep Cross Network to evaluate diabetes risks based on Gen-Z lifestyle inputs.

The repository is divided into two primary environments:
- `Modeling` — Data exploration, custom TensorFlow architecture design, and training artifacts.
- `Deployment` — Resources and configurations to serve the model as a scalable FastAPI service.

## 🧠 Folder: Modeling (The ML Brain)
The `Modeling` directory is the laboratory where the analytical rigor of SugarCoat.ai is forged. We moved beyond traditional tabular models to implement a deep learning architecture capable of understanding the fatal synergies of bad habits.

**Core ML Architecture:**
*   **Algorithm:** **Deep Cross Network (DCN)** built via TensorFlow Functional API. DCN was selected to automatically learn explicit feature crossings.
*   **Classification Strategy:** **Binary** (`Normal` & `Diabetes`) utilizing `binary_crossentropy` to pinpoint the critical point of users before irreversible damage occurs.
*   **Custom TensorFlow Components:**
    *   `RiskAmplifierLayer`: A custom architectural layer engineered to mathematically penalize high-risk lifestyle intersections.
    *   `TrainingMonitor`: A dynamic custom callback for real-time validation tracking, learning rate adjustments, and preventing model overfitting.
*   **Export Pipeline:** The model is serialized as a stateless `.keras` artifact.

**Directory Contents:**
*   `dataset_sugarcoat.csv` — The foundational tabular dataset for predictive modeling.
*   `[Modelling]_SugarCoat_ai.ipynb` — The master notebook containing EDA, DCN architecture definition, custom component classes, and the training loop.
*   `logs/fit/` — TensorBoard log directory for training and validation metrics monitoring.

## 🚀 Folder: Deployment (The Inference Engine)
The `Deployment` folder contains the production-ready environment required to serve the trained SugarCoat.ai model as a high-performance FastAPI endpoint.

**Deployment Mechanics:**
*   **Custom Object Loading:** The FastAPI server dynamically loads `sugarcoat_model.keras`.
*   **Stateless Inference:** The API processes incoming JSON payloads, applies the serialized `joblib` scalers, and outputs the precise multiclass probability distribution utilized by our Generative AI pipeline.

**Directory Contents:**
*   `Dockerfile` — Docker image configuration utilizing `python:3.10-slim` for a lightweight, production-ready container.
*   `main.py` — The FastAPI application script handling the routing, model loading, and `/predict` endpoint execution.
*   `requirements.txt` — Python dependencies required strictly for the server environment.
*   `sugarcoat_model.keras` — The finalized, trained TensorFlow DCN artifact.

**Live API Endpoints (Hugging Face Spaces):**
*   **FastAPI Application:** [https://Ifanhakm-sugarcoat-api.hf.space](https://Ifanhakm-sugarcoat-api.hf.space)
*   **OpenAPI Documentation (Swagger):** [https://Ifanhakm-sugarcoat-api.hf.space/docs](https://Ifanhakm-sugarcoat-api.hf.space/docs)
*   **Inference Endpoint:** [https://Ifanhakm-sugarcoat-api.hf.space/predict](https://Ifanhakm-sugarcoat-api.hf.space/predict)

## 🔄 Workflow Summary
1. **Train & Iterate:** Data engineering and model training are executed strictly within the `Modeling` directory.
2. **Artifact Transfer:** Upon achieving optimal validation metrics, the `sugarcoat_model.keras` and preprocessor files are exported to the `Deployment` directory.
3. **Serve & Scale:** The `Deployment` folder acts as the standalone codebase for local execution or containerized deployment on Hugging Face Spaces.
