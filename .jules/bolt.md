## 2024-05-24 - IsolationForest Inference Redundancy
**Learning:** Calling both `predict(X)` and `decision_function(X)` on Scikit-Learn's IsolationForest doubles the inference time because `predict()` internally calls `decision_function()`.
**Action:** Calculate `decision_function(X)` once and derive predictions manually using `np.where(scores < 0, -1, 1)` or direct mapping to avoid the redundant internal call.
