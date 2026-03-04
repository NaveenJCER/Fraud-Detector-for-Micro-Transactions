## 2024-05-24 - [IsolationForest Inference Optimization]
**Learning:** For scikit-learn's `IsolationForest`, calling both `predict()` and `decision_function()` computes tree transversals twice.
**Action:** Always call `decision_function(X)` once and map scores (<0 for anomalies) manually to avoid redundant compute and halve inference time.
