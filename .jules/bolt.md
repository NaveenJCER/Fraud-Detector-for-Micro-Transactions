## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-19 - Redundant DataFrame filtering in Streamlit dashboard
**Learning:** Streamlit renders UI sequentially. Filtering a DataFrame multiple times for different metrics (e.g., `df[df['anomaly_flag'] == 'Fraud']` for length, then again for displaying) causes unnecessary performance overhead.
**Action:** Always filter the DataFrame once, store it in a variable, and reuse it for all subsequent calculations and rendering calls to optimize processing time.
