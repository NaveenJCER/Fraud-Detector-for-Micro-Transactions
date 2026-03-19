## 2026-03-19 - IsolationForest inference optimization
**Learning:** IsolationForest.predict(X) internally calls decision_function(X) to determine the threshold. When both anomaly flags and raw scores are needed, calling both predict(X) and decision_function(X) traverses the trees twice, doubling the inference time.
**Action:** Always call decision_function(X) once and manually derive the anomaly flags (score < 0 indicates anomaly) using np.where to halve the computation time.
