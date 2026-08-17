## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-15 - Streamlit redundant DataFrame filtering
**Learning:** In Streamlit applications, redundant pandas DataFrame filtering (e.g. repeated calls to `df[df['anomaly_flag'] == 'Fraud']` for metrics and table rendering) doubles execution time on every render cycle.
**Action:** Always cache filtered DataFrame subsets in variables and reuse them for multiple operations to achieve >2x speedup on data processing.
