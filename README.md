# 🍩 SugarCoat.ai
> *We don't sugarcoat your health risks. We roast them.*

[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Generative AI](https://img.shields.io/badge/Generative_AI-Magic-8A2BE2?style=for-the-badge)](#)

SugarCoat.ai is a preventative health assistant engineered specifically to pierce through the apathy of Generation Z. By combining the analytical rigor of **Machine Learning** with the unapologetic, "savage" persona of **Generative AI**, this platform measures diabetes risk through low-friction lifestyle inputs and responds with data-driven, sarcastic guilt-trips designed to catalyze real behavioral change.

## 🚀 The Core Experience
*   **Progressive Profiling:** We evaluate baseline risks using daily lifestyle habits (e.g., extreme screen time, sweet beverage consumption) rather than demanding high-friction clinical data upfront.
*   **The "Savage" AI Persona:** Traditional medical apps are rigid and easily ignored. SugarCoat.ai breaks the mold by delivering hyper-personalized, factual "roasts" that act as psychological hooks, compelling users to take genuine medical lab tests.
*   **Action-Oriented Catalyst:** Every sarcastic interaction is algorithmically tethered to a strict medical disclaimer and a call-to-action for professional medical validation.

## 🧠 Machine Learning Architecture
Our backend is not a simple API wrapper. The risk prediction engine is built on an advanced, production-ready pipeline:
*   **Core Architecture:** **Deep Cross Network (DCN)** built via the TensorFlow Functional API to automatically learn complex, explicit feature crossings (e.g., the compounded fatal risk of high sugar intake combined with a sedentary lifestyle).
*   **Classification Strategy:** **Multiclass Classification** targeting three absolute zones: `Normal`, `Prediabetes`, and `Type 2 Diabetes`, optimized using the `sparse_categorical_crossentropy` loss function.
*   **Custom TensorFlow Components:** 
    *   `RiskAmplifierLayer`: A custom architectural layer designed to penalize specific, fatal combinations of bad lifestyle habits.
    *   `TrainingMonitor`: A dynamic custom callback implemented to govern the learning rate and prevent overfitting during the training phase.
*   **Deployment Pipeline:** The model is exported as a stateless `.keras` artifact. During inference, it is dynamically loaded alongside custom objects (`custom_objects`) and stateful preprocessors (`LabelEncoder`, `StandardScaler`) serialized via `joblib`.

## 📂 Repository Structure
```text
📦 SugarCoat.ai
 ┣ 📂 deployment/          # Server configuration & Gen-AI prompt pipeline
 ┣ 📂 modeling/            # Jupyter notebooks, dataset EDA, & model training
 ┃ ┣ 📜 dataset_sugarcoat.csv
 ┃ ┣ 📜 [Modelling]_SugarCoat_ai.ipynb
 ┃ ┗ 📂 custom_components/ # Source code for RiskAmplifierLayer & TrainingMonitor
 ┣ 📂 frontend/            # Client-side interface
 ┣ 📜 .gitignore
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
 ```

## ⚙️ Quick Start (Local Setup)

Clone the repository:
```Bash
git clone [https://github.com/username/sugarcoat-ai.git](https://github.com/username/sugarcoat-ai.git)
cd sugarcoat-ai
```

Install dependencies:
```Bash
pip install -r requirements.txt
```

Run the Backend Server:
```Bash
cd deployment
uvicorn main:app --reload
```

## 👥 The Engineering Team
Developed as a Capstone Project for the DBS Foundation Coding Camp.
- Ifan Hakim - AI/ML Engineer
- Lia Rahma Asnaini - AI/ML Engineer
- Dandy Faishal Fahmi - Fullstack Developer
- Daffa Pandora El-farisin - Fullstack Developer
- Rafi Abdul Rosid - Data Scientist
- Java Langit Jingga - Data Scientist

_Disclaimer: SugarCoat.ai operates exclusively as an Early-Warning System. Final medical diagnoses must rely on professional clinical laboratory tests._