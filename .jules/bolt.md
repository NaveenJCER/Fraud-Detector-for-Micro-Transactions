## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-24 - Streamlit UI Rendering Order
**Learning:** Streamlit renders UI elements sequentially based on their execution order in the Python script. Moving logical assignments (like filtering a DataFrame) higher in the script to optimize them can inadvertently alter the layout if UI elements (like `st.subheader`) are moved along with them.
**Action:** Always separate logic optimization from UI rendering. Ensure that UI components (e.g., `st.subheader`, `st.markdown`) remain in their original positions in the script, even if the data they consume is calculated earlier.
