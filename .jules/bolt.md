## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-15 - Redundant DataFrame Filtering
**Learning:** In Streamlit apps, redundant pandas DataFrame filtering (like `df[df['anomaly_flag'] == 'Fraud']`) is often repeated for metrics and later components. This duplicates operations on the same data.
**Action:** Always cache the filtered subset in a variable initially and reuse it across the app to achieve a measurable speedup (often >2x) without changing visual output.
