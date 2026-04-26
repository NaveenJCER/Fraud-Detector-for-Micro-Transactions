## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-24 - Streamlit Frontend Rendering vs State Ordering
**Learning:** In Streamlit, UI elements are rendered sequentially based strictly on the order of Python execution. When refactoring variables to optimize performance (like moving a DataFrame filter up to avoid redundancy), moving the variable initialization is safe, but inadvertently moving associated rendering calls (like `st.subheader`) will break the visual order of the dashboard.
**Action:** Always separate data state initialization from UI rendering blocks when optimizing Streamlit scripts, ensuring rendering functions remain in their original chronological order.
