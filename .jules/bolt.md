## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-07-28 - Redundant Pandas Filtering in Streamlit
**Learning:** Streamlit scripts re-run top-to-bottom on every interaction. Redundant Pandas DataFrame filtering operations (like `df[df['col'] == val]`) in the main script body cause unnecessary repeated O(N) operations, which slows down the UI rendering.
**Action:** Cache the result of dataframe filtering operations in variables and reuse them across metrics and rendering logic to avoid redundant operations and speed up execution.
