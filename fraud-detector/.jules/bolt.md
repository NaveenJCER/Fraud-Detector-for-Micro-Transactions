## 2024-03-10 - IsolationForest redundant predictions
**Learning:** Calling both `predict(X)` and `decision_function(X)` on scikit-learn's `IsolationForest` doubles inference time because `predict()` internally computes `decision_function()` under the hood.
**Action:** Always compute `decision_function(X)` once and derive predictions manually (e.g. using `np.where(scores < 0, -1, 1)`) to effectively halve inference latency.
