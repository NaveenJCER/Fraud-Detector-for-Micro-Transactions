## 2024-05-24 - [IsolationForest Double Evaluation]
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)`. Calling both `predict(X)` and `decision_function(X)` sequentially evaluates the trees twice.
**Action:** Call `decision_function(X)` once and manually derive predictions (`np.where(scores < 0, -1, 1)`) to halve inference time.
