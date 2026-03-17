## 2024-03-17 - [IsolationForest Redundant Prediction Optimization]
**Learning:** scikit-learn's IsolationForest model calculates `decision_function(X)` internally when `predict(X)` is called. If both anomaly flags and raw scores are needed, calling both methods results in identical redundant computations.
**Action:** When both labels and scores are required from an IsolationForest, always calculate `decision_function(X)` once and derive labels manually via `np.where(score < 0, -1, 1)` to effectively halve the inference execution time.
