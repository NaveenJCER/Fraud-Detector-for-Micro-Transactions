## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-07-14 - Redundant Pandas Filtering in Streamlit
**Learning:** Redundant pandas filtering (e.g., multiple calls to `df[df['col'] == 'value']`) can significantly slow down the rendering of data visualization interfaces, wasting CPU cycles on operations that can be cached.
**Action:** Always cache the result of the first filtering operation in a variable and reuse it for subsequent metrics and rendering to achieve a >2x performance speedup.
