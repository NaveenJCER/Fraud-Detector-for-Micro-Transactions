## 2025-02-14 - Optimized Isolation Forest Prediction
**Learning:** In Scikit-learn's IsolationForest, calling predict(X) internally computes the decision_function(X) again. If you need both the label and the score, it's faster to compute decision_function(X) once and derive the label yourself (score < 0 means anomaly). This saves redundant tree traversals.
**Action:** When using tree-based anomaly detection models where scores and labels are needed, always compute scores first and derive labels to avoid double computation.
