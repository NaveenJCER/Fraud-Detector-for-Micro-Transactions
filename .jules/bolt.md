## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-24 - Streamlit Pandas Filtering Optimization
**Learning:** In Streamlit apps, repeatedly filtering Pandas DataFrames for the same condition across different sections blocks the main thread unnecessarily and slows down rendering.
**Action:** Cache the filtered DataFrame in a variable and reuse it for metrics and rendering to avoid redundant operations and achieve measurable performance speedups.
