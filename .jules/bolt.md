## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-15 - Redundant Pandas Filtering in Streamlit
**Learning:** Computing the same filtered DataFrame (e.g., `df[df['flag'] == 'value']`) multiple times for metrics and rendering duplicates expensive work and blocks the thread.
**Action:** Always cache the filtered subset in a variable (e.g., `subset = df[...]`) and reuse it for length checks and subsequent rendering.
