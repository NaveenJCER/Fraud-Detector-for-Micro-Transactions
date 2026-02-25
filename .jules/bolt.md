## 2025-05-18 - Scikit-Learn IsolationForest Performance
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)`. Calling both sequentially (e.g., to get both labels and scores) triggers a double traversal of the isolation trees, which is redundant and expensive.
**Action:** When both predictions and scores are needed, call `decision_function(X)` once and derive the predictions manually using `np.where(score < 0, -1, 1)`. This results in a ~50% speedup for inference.
