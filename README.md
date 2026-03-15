# Appendicitis-Severity-Prediction-PowerBI
## Diagnosing Inefficiencies in Emergency Care: A Predictive Dashboard for Appendicitis Severity 🏥

**Microsoft Elevate Capstone Project - Power BI Track**

### 📌 Project Overview
Appendicitis is a critical tracer condition for evaluating the efficiency of emergency healthcare triage. Delayed or inaccurate diagnoses can escalate a standard procedure into a severe complication (rupture), significantly increasing patient risk and hospital costs.

This project is a dynamic epidemiological surveillance and triage tool built entirely within **Power BI**. It integrates a **Random Forest Machine Learning model** directly into the data ingestion pipeline via Power Query (Python) to predict the severity of appendicitis at the moment of admission, using only preliminary triage data and blood biomarkers.

### 🎯 Problem Statement & Solution
* **The Problem:** Current triage systems rely heavily on subjective patient pain scales and standard ultrasound imaging (which frequently fails to visualize the appendix). Furthermore, delaying triage past 48 hours exponentially compounds baseline inflammation.
* **The Solution:** A deployable BI dashboard that acts as a transparent AI safety net. It analyzes patient vitals, demographics, and lab results in real-time to generate a `Predicted_Severity` class and `Prediction_Confidence` score, allowing hospital administrators to prioritize surgical beds based on objective statistical risk.

### 📊 Key Clinical & Analytical Insights
* **Biomarkers Outperform Subjective Symptoms:** The algorithm identified that a Neutrophil percentage exceeding 69.9% is the dominant predictor of severity, making a patient **11.78 times more likely** to suffer a complication.
* **The 48-Hour Escalation Point:** Temporal analysis proves that delaying surgical intervention past the 48-hour and 72-hour thresholds exponentially compounds inflammation (CRP) and rupture risk.
* **Volume vs. Vulnerability:** While the 21–30 age bracket drives the highest volume of ER admissions, the proportional risk of severe complications is disproportionately concentrated in pediatric patients, seniors, and overweight BMI profiles.
* **Model Validation & Triage Safety:** The Random Forest model achieved a **79% Test Accuracy** on unseen hold-out data. More importantly for clinical safety, the dashboard actively isolates and tracks a **20% False Negative Rate**, providing a quantifiable baseline to ensure severe cases are not accidentally discharged.

### 🛠️ Tech Stack & Architecture
* **Data Visualization & BI:** Power BI, DAX (Custom Measures & Field Parameters)
* **Machine Learning:** Python (`scikit-learn`, `pandas`) 
* **Integration:** Python script executed natively within Power BI Power Query for automated data preprocessing, label encoding, and model scoring.
* **Algorithm:** Random Forest Classifier (`n_estimators=100`, `class_weight='balanced'`)

### 📂 Repository Contents
* `Appendicitis_Surveillance_Dashboard.pbix`: The complete, interactive Power BI dashboard file.
* `model_fitting.py`: The Python script utilized within Power Query for data transformation and ML predictions.
* `appendicitis_comprehensive_dataset.csv`: The clinical dataset utilized for training the model and populating the visuals.

### 👨‍💻 Author
**Tuhin Adak** *B.Sc. Statistics (Honours) | Ramakrishna Mission Residential College, Narendrapur*
*Microsoft Elevate Intern (Power BI Track)*
