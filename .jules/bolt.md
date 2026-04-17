## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-17 - Vectorized timestamp generation
**Learning:** Generating timestamps using a Python list comprehension and `random.randint` with `timedelta` in a loop over a large dataset is slow.
**Action:** Always vectorize timestamp generation using `pd.Timestamp`, `np.random.randint`, and `pd.to_timedelta` which is significantly faster.
