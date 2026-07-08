## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-07-08 - Streamlit redundant DataFrame filtering
**Learning:** Streamlit apps often re-filter the same DataFrame for different components (e.g., calculating metrics at the top, rendering tables at the bottom). Repeating `df[df['col'] == val]` is an unnecessary operation per render cycle.
**Action:** Always filter DataFrames once at the top level and cache the subset in a variable to reuse for both metrics and subsequent UI rendering, achieving measurable speedup.
