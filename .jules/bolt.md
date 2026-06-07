## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Redundant pandas filtering in Streamlit
**Learning:** Streamlit apps often re-calculate values sequentially. Redundantly filtering pandas DataFrames (e.g., `df[df['flag'] == 'X']`) for both metrics and rendering duplicates O(N) operations, which scales poorly.
**Action:** Always cache filtered DataFrames if the subset is reused for metrics and display logic further down the script.
