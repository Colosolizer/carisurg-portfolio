### **Project summary**

The CariSurg Triage Project delivers a modular, machine learning-driven pipeline designed to predict the Emergency Severity Index (ESI) for patients entering the emergency department. It is built for Clinical IT teams and emergency physicians to augment clinical decision-making by providing predictive severity scores based on initial patient vitals, clinical indicators, and triage flow data.

### **Final-model decision**

The Random Forest Classifier was selected as the final model because it demonstrated superior robustness in handling the class imbalance inherent in clinical triage datasets, particularly when utilizing the balanced class weight configuration.

### **How to run**

1. **Clone**: Clone the repository to your local machine.  
2. **Install**: Create and activate a virtual environment, then install dependencies: pip install \-r requirements.txt.  
3. **Python**: Execute the training pipeline from the root directory: python scripts/train.py \--config config.yaml.  
   * Note: Always run pytest tests/test\_carisurg.py before to ensure the data schema and training pipeline are functioning correctly.

### **Where the data lives**

* **Path**: The raw clinical dataset is stored in data/yaleemmlc\_admissionprediction\_triage.csv.  
* **Governance**: Access is strictly regulated by Clinical IT protocols; all data handling must comply with HIPAA and institutional privacy standards.  
* **Status**: The pipeline is currently in a production-ready state, with automated tests (schema checks and smoke tests) enforced to validate data integrity upon ingestion.  
    
    
    
    
  


### **Known limitations**

* **Vital Sign Dependency**: The model relies on the accuracy of initial vitals, missing or erroneous data (e.g., failed BP cuff readings) significantly impacts the prediction output.  
* **Generalizability**: The model was trained on a specific institutional dataset; performance may drift when applied to patient populations with different demographic profiles without re-calibration.  
* **Algorithmic Fairness**: While the code allows for demographic encoding, the model must undergo periodic audit to ensure predictions remain equitable across different patient groups, as "failing loudly" is required to prevent silent bias.

### **Who to ask**

* **Model/Code Questions**: Lead Data Scientist (Project Owner).  
* **Data Access & Governance**: Clinical IT Department.  
* **Clinical/Triage Workflow**: Clinical Lead / Attending Physician.

