## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-07-12 - Redundant pandas DataFrame filtering
**Learning:** Repeatedly filtering a pandas DataFrame with the same condition (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for metrics and later for rendering duplicates the cost of the boolean mask creation and indexing operation.
**Action:** Always evaluate filtering conditions once, cache the resulting subset in a local variable, and reuse it across multiple operations to cut evaluation time in half and improve UI responsiveness.
