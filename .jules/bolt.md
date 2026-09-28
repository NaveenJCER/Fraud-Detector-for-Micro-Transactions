## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2026-09-28 - Redundant DataFrame filtering in Streamlit
**Learning:** In Streamlit apps, the entire script reruns on every interaction. If you perform the same DataFrame filtering operation (e.g., `df[df['flag'] == 'X']`) multiple times for different UI components, it duplicates O(N) work on every render cycle.
**Action:** Always cache filtered DataFrame subsets into a variable early in the script and reuse them across summary metrics, charts, and tables to minimize redundant processing.
