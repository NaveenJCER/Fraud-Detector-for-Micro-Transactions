## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Redundant DataFrame Filtering in Streamlit
**Learning:** Streamlit reruns the script on every interaction. Filtering pandas DataFrames is computationally expensive, especially on large datasets. If the same filtered subset (like `df[df['anomaly_flag'] == 'Fraud']`) is used multiple times (e.g., for metrics calculation and rendering), calling it twice doubles the overhead.
**Action:** Always extract and cache repeated DataFrame filtering operations into variables to prevent redundant execution and improve Streamlit rendering performance.
