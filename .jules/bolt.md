## 2024-05-23 - IsolationForest Efficiency
**Learning:** Scikit-learn's `IsolationForest.predict()` internally calls `decision_function()` and thresholds the result. Calling both methods sequentially on the same data doubles the inference cost unnecessarily.
**Action:** When needing both the anomaly label and the score, call `decision_function()` once and manually threshold the result (score < 0 for anomaly) instead of calling `predict()`.
