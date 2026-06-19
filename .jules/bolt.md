## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-01 - Prevent redundant pandas filtering in Streamlit
**Learning:** Repeatedly filtering a DataFrame in a Streamlit app (e.g., `df[df['anomaly_flag'] == 'Fraud']`) re-executes on every render, wasting CPU. Caching the subset in a variable prevents redundant work and doubles speed.
**Action:** Assign frequently filtered pandas subsets to a variable and reuse it for lengths or rendering instead of filtering multiple times.
