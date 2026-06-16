## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Streamlit redundant pandas filtering
**Learning:** In Streamlit apps, repeated pandas DataFrame filtering (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for summary metrics and subsequent rendering causes redundant processing.
**Action:** Cache the filtered subset in a variable first, and reuse it for computing metrics (`len(frauds)`) and UI rendering to achieve measurable performance speedup.
