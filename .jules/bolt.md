## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-07-04 - Caching pandas filtered DataFrames
**Learning:** In Streamlit apps, assigning a filtered pandas DataFrame to a variable and then calculating `len()` is over 2x faster than performing the same boolean filtering twice (once for length, once for display). Repeated filtering creates redundant DataFrame copies.
**Action:** Always cache the result of a boolean filter (e.g., `frauds = df[...]`) and reuse it for derived metrics and rendering instead of recalculating it.
