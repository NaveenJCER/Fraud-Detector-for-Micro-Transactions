## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-11-20 - Redundant DataFrame filtering in Streamlit
**Learning:** In Streamlit apps, redundant DataFrame filtering (e.g., repeatedly calling `df[df['anomaly_flag'] == 'Fraud']` for metrics and rendering) doubles the execution time of that operation on every re-render.
**Action:** Always cache the filtered subset in a variable and reuse it across the application to achieve a measurable >2x performance speedup.
