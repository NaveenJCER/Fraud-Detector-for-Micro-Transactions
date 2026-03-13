## 2024-05-28 - Optimize Isolation Forest inference
**Learning:** `IsolationForest.predict(X)` calculates `decision_function(X)` internally. If a project needs both predictions and scores, calling both `predict()` and `decision_function()` effectively runs the anomaly detection logic twice.
**Action:** Always compute `decision_function(X)` once and derive predictions manually using `np.where(score < 0, -1, 1)` to halve the inference time when both are needed.
