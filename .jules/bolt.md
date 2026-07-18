## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-20 - Streamlit redundant DataFrame filtering
**Learning:** Redundant pandas DataFrame filtering (e.g., repeated calls to `df[df['anomaly_flag'] == 'Fraud']`) inside a Streamlit app slows down render time unnecessarily as the same scan runs multiple times.
**Action:** Always cache the filtered subset in a variable and reuse it for metrics and rendering to achieve measurable >2x performance speedup.
