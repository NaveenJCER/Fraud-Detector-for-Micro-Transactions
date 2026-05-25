## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-25 - Redundant DataFrame filtering in Streamlit
**Learning:** Redundant pandas DataFrame filtering (e.g., repeatedly calling `df[df['anomaly_flag'] == 'Fraud']`) can cause significant performance slowdowns, especially as the dataframe size grows.
**Action:** Always assign the result of a dataframe filter to a variable if the subset is needed multiple times to avoid expensive re-evaluation.
