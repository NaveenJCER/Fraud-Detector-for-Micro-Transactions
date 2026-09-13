## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-24 - Streamlit redundant Pandas filtering
**Learning:** Streamlit executes top-to-bottom on every interaction. Redundant Pandas DataFrame filtering (e.g., `df[df['anomaly_flag'] == 'Fraud']` calculated multiple times for metrics and display) becomes a significant bottleneck as data scales.
**Action:** Always cache filtered dataframes in variables and reuse them throughout the Streamlit script to avoid duplicated O(N) operations on every render.
