## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2025-02-15 - Streamlit redundant DataFrame filtering
**Learning:** In Streamlit apps, recalculating the same DataFrame subset (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for metrics and later for display introduces redundant computation overhead. However, moving variable assignments to cache the subset must be done carefully because Streamlit renders UI elements sequentially; moving rendering calls along with assignments will cause visual regressions.
**Action:** Always cache frequently used DataFrame subsets into variables at the earliest logical point in the script, ensuring that only the data assignment is moved, while preserving the original sequential order of UI rendering calls (like `st.subheader`).
