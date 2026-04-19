## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-04-19 - Streamlit Redundant DataFrame Filtering
**Learning:** In Streamlit applications, repeatedly filtering a large DataFrame (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both metric calculation and rendering causes duplicate O(N) operations on every re-render. Benchmarks showed extracting this into a variable improves execution speed by ~50% for that path.
**Action:** Always store filtered DataFrames in variables and reuse them across summary metrics and visualization components to minimize CPU cycles.
