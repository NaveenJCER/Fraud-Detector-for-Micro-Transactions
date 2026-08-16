## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-08-16 - Redundant Pandas Filtering in UI
**Learning:** Redundantly filtering a Pandas DataFrame (e.g., `df[df['flag'] == 'Fraud']`) for both metric calculation and rendering in a Streamlit app introduces measurable overhead.
**Action:** Always cache the filtered subset in a variable and reuse it across metrics and rendering to achieve >2x performance speedup in the segment.
