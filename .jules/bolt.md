## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-15 - Redundant Pandas Filtering in Streamlit Apps
**Learning:** In Streamlit applications, repeatedly filtering Pandas DataFrames (like `df[df['flag'] == 'Val']`) for different UI components triggers redundant O(N) operations, measurably slowing down rendering when datasets are large.
**Action:** Always cache filtered DataFrames in variables and reuse them across metrics and rendering logic to cut redundant calculation times.
