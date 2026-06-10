## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-10-24 - Streamlit Sequential Execution & Redundant Filtering
**Learning:** In Streamlit apps, sequentially evaluating redundant Pandas DataFrame filters (e.g., `df[df['flag'] == 'X']` for metrics, then again for rendering tables) doubles the evaluation time. However, because Streamlit renders UI elements exactly where their Python calls occur, variable assignments must be moved without moving the UI rendering calls (like `st.subheader`) to avoid visual regressions.
**Action:** Cache filtered subsets in a variable early in the script execution flow, and reuse them for both metrics and rendering, being careful not to alter the order of UI rendering functions.
