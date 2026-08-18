## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-08-18 - Streamlit Redundant DataFrame Filtering
**Learning:** In Streamlit apps, repeatedly filtering Pandas DataFrames (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for metrics and then again for rendering wastes computation.
**Action:** Always cache the filtered DataFrame in a variable and reuse it (e.g., `frauds = df[...]`, then `len(frauds)`), halving the filtering overhead.
