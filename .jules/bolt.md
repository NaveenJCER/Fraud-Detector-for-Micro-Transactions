## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2026-10-05 - Cache Streamlit DataFrames
**Learning:** Repeatedly filtering DataFrames (e.g. `df[df['flag'] == 'X']`) for both length metrics and rendering component duplicates expensive pandas operations unnecessarily.
**Action:** Always filter the DataFrame once, save it to a variable, and reuse it for both metrics and rendering to improve performance.
