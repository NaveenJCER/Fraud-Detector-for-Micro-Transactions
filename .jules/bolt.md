## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Redundant Pandas DataFrame Filtering
**Learning:** Repeatedly evaluating `df[df['anomaly_flag'] == 'Fraud']` across multiple lines for different calculations (e.g., getting lengths vs retrieving data rows) performs redundant O(N) operations, which measurably degrades performance as dataset size grows.
**Action:** Always filter DataFrames once into a cached variable and reuse that subset for all downstream calculations and renderings in UI components.
