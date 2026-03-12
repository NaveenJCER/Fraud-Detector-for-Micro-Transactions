## 2024-03-12 - [IsolationForest Double Invocation Anti-Pattern]
 **Learning:** [Calling both `predict(X)` and `decision_function(X)` on Scikit-Learn's IsolationForest results in redundant O(N) tree traversals since `predict()` internally invokes `decision_function()` under the hood. This effectively doubles inference time.]
 **Action:** [Calculate `decision_function(X)` once and derive predictions manually using `np.where` (e.g., score < 0 indicates anomaly) to avoid the redundant call, halving inference time.]
