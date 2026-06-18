## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-15 - Streamlit UI rendering order vs logic refactoring
**Learning:** Streamlit renders UI elements sequentially based on their execution order in the Python script. When refactoring logic (like hoisting variable assignments for caching/optimization to avoid redundant data processing), moving UI rendering calls (like `st.subheader`) out of order will cause visual regressions in the dashboard.
**Action:** When caching redundant computations in Streamlit, separate data logic from rendering. Move only the data processing logic (e.g., DataFrame filtering) to the top, and leave all `st.*` rendering calls in their original sequence.
