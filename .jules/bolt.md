## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-15 - Streamlit Redundant Filtering
**Learning:** Streamlit renders sequentially and reruns on every interaction. Redundant DataFrame filtering (e.g., `df[df['flag'] == 'Fraud']`) for metrics and later for display can cause measurable slowdowns (>2x) since the O(N) operation is duplicated.
**Action:** Always cache the filtered subset in a variable and reuse it for both metric calculations and UI rendering to avoid repeated computation overhead while maintaining execution order for visual components.
