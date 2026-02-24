## 2024-05-23 - [Scikit-Learn IsolationForest Optimization]
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` and thresholds the result. Calling both separately (e.g., to get both label and score) results in redundant tree traversals, doubling the inference time.
**Action:** When both prediction and score are needed, call `decision_function(X)` once and derive the prediction manually using `np.where(score < 0, -1, 1)` (or mapped labels). This yields a ~50% performance improvement.
