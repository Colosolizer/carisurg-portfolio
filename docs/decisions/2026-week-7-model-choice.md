### **Decision Journal: 2026-Week-7-Model-Choice**

**Context**

* Our current baseline (Logistic Regression) is failing to meet the required safety threshold for ESI 1 recall, identifying only 25% of resuscitation-level patients.  
* We must select a model that balances clinical safety (Recall for ESI 1\) with operational constraints (Inference time and Interpretability) to prepare for a pilot implementation.


**Alternatives Considered**

* **Logistic Regression:** Retaining our baseline, which offers high interpretability but lacks the complexity to capture the non-linear patient features required for effective ESI 1 detection.  
* **Gradient Boosting:** Exploring this model for its superior aggregate metrics, though it presents significant risks regarding 'black box' behaviour and higher inference costs.  
* **Tuned Random Forest:** Evaluating this as an intermediate model that might offer improved recall over our baseline without the high technical barrier of Gradient Boosting.


**Decision**  
I have decided to move forward with the Tuned Random Forest model for our next development phase, as it provides the optimal 'honest middle ground' for our current clinical requirements.

**Reasoning**

* **Performance (Recall ESI 1 axis):** The Tuned Random Forest achieved an ESI 1 recall of 0.312, demonstrating a clear performance gain over the Logistic Regression baseline (0.250) in capturing life-saving cases.  
* **Interpretability (Explain axis):** Unlike Gradient Boosting, which is harder to explain, the Random Forest maintains a 'Medium' interpretability level that allows us to leverage feature importances for initial clinical discussions.  
* **Efficiency (Infer axis):** While the inference time (0.105ms) is higher than the baseline, it remains well within the operational limits for a high-volume emergency department setting, representing an acceptable trade-off for the improved recall.


**Things Not Yet Known**

* Whether applying class\_weight='balanced' during training will further improve ESI 1 recall without degrading performance on mid-acuity (ESI 3\) cases.  
* Whether the clinical team will find the 'Medium' interpretability level of Random Forest sufficiently transparent to build trust during the initial shadowing phase.

