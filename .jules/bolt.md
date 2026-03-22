## 2024-05-24 - IsolationForest Inference Optimization
**Learning:** Calling `predict(X)` and `decision_function(X)` sequentially on an `IsolationForest` causes redundant internal tree traversals, effectively doubling inference time.
**Action:** Always calculate `decision_function(X)` once and derive predictions manually using `np.where(scores < 0, -1, 1)` to halve inference time.
