## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-08-07 - Redundant DataFrame filtering in Streamlit
**Learning:** Evaluating the exact same DataFrame filter (like `df[df['anomaly_flag'] == 'Fraud']`) multiple times for different purposes (e.g., once for calculating length, later for displaying the filtered data) creates unnecessary duplicated computation on every re-render.
**Action:** Always cache the result of the filter into a variable first (e.g., `frauds = df[...]`), and reuse that variable for lengths (`len(frauds)`) and display, yielding significant speedups.
