## 2025-03-25 - [IsolationForest Inference Duplication]
**Learning:** scikit-learn's `IsolationForest.predict(X)` internally calls `decision_function(X)`. Calling both sequentially to extract labels and scores doubles the computational cost unnecessarily.
**Action:** When both predictions and scores are needed, calculate `decision_function(X)` once and derive the anomaly flags manually using `np.where(score < 0)` to halve inference time.
