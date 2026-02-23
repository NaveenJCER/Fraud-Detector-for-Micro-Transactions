## 2026-02-13 - [Scikit-Learn IsolationForest Performance]
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)`. If you need both the binary prediction and the anomaly score, calling them separately causes redundant tree traversals.
**Action:** When both are needed, call `decision_function(X)` first and manually derive predictions (`score < 0` => anomaly). This reduces inference time by ~45-50%.
