## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-15 - Streamlit redundant pandas DataFrame filtering
**Learning:** In Streamlit apps, repeatedly filtering a pandas DataFrame for the same condition (e.g., once for metrics, again for displaying tables) causes the O(N) mask-based indexing to execute multiple times during every re-render.
**Action:** Always cache the filtered subset in a variable and reuse it for metrics and rendering to achieve a measurable >2x performance speedup.
