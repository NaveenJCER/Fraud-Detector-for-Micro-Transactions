## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-24 - Redundant pandas filtering in Streamlit rendering
**Learning:** Streamlit re-evaluates the entire script on UI interactions. Evaluating the same pandas filter condition like `df[df['anomaly_flag'] == 'Fraud']` multiple times per render (e.g., once for metrics, once for a table) duplicates O(N) operations unnecessarily and significantly slows down the frontend responsiveness.
**Action:** Always evaluate pandas boolean masks once per render loop, store the result in a variable, and reuse it for metrics and rendering components to halve computation time.
