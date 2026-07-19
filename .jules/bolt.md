## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-01 - Streamlit redundant pandas filtering
**Learning:** Streamlit apps rerun top-to-bottom on interaction. Doing the same pandas DataFrame filtering (e.g. `df[df['col'] == 'val']`) twice (once for length, once for rendering) duplicates work on every single render cycle.
**Action:** Always cache the result of expensive DataFrame filters into a variable and reuse it throughout the Streamlit script to achieve >2x speedup on those operations.
