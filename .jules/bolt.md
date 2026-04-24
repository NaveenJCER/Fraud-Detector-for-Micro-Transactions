## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2026-04-24 - Cached Filtered DataFrame in Streamlit
**Learning:** Streamlit renders UI elements sequentially based on their execution order in the Python script. When refactoring logic (e.g., moving variable assignments for optimization), ensure UI rendering calls (like st.subheader) are not inadvertently moved, as this will cause visual regressions in the dashboard.
**Action:** Always store the filtered result in a variable and reuse it to minimize memory allocations and CPU cycles while keeping UI components in their original order.
