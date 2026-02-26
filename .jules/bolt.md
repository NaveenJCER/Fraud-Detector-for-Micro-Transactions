## 2025-02-26 - Optimization of Scikit-Learn IsolationForest
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` and thresholds the result. Calling both separately performs the expensive tree traversal twice.
**Action:** When both anomaly flags and scores are needed, calculate `decision_function` once and derive predictions manually (score < 0 is anomaly). This yields ~2x speedup for inference.
