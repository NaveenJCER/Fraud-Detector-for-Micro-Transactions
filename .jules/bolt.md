## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-02 - Redundant DataFrame filtering in Streamlit
**Learning:** Performing multiple identical conditional filterings on large pandas DataFrames (e.g. `df[df['anomaly_flag'] == 'Fraud']` to get counts, and then again later to get a subset for rendering) creates unnecessary duplicate computation and memory allocation overhead.
**Action:** Always cache the filtered DataFrame in a variable and reuse it for both metric extraction (e.g., `len(frauds)`) and further processing/rendering to achieve a >2x performance speedup.
