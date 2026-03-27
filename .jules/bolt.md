## 2024-05-23 - IsolationForest Performance Optimization
**Learning:** Scikit-Learn's `IsolationForest.predict()` method internally recalculates the `decision_function()` scores, meaning calling both `predict()` and `decision_function()` on the same input data performs redundant computation.
**Action:** When both anomaly flags and raw scores are needed from an `IsolationForest` model, only call `decision_function(X)`. Derive the anomaly flags manually using `np.where(scores < 0, -1, 1)` to halve the inference time.
