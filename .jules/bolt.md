## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-24 - Cache Pandas Filtering in Streamlit Apps
**Learning:** In Streamlit apps, repeatedly filtering pandas DataFrames (e.g., `df[df['condition'] == 'value']`) for both metrics and UI rendering duplicates the same exact work on every single app rerun.
**Action:** Always extract frequently filtered DataFrame subsets into a variable and reuse it across multiple widgets or calculations to prevent redundant pandas filtering operations.
