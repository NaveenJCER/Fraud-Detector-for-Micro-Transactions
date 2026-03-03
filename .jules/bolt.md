## 2023-10-25 - Avoid Redundant Computations in IsolationForest Inference
**Learning:** Scikit-Learn's `IsolationForest.predict(X)` internally calls `decision_function(X)`. Calling both `.predict(X)` and `.decision_function(X)` results in redundantly calculating scores, effectively doubling inference time and CPU utilization.
**Action:** Always compute `scores = model.decision_function(X)` once and derive predictions manually (e.g., `np.where(scores < 0, "Fraud", "Legit")`) to halve inference time while preserving the same logic.
