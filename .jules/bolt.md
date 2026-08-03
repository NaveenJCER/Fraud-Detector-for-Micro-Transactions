## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-18 - Pandas vectorized datetime generation
**Learning:** Using Python list comprehensions with `datetime` and `timedelta` is significantly slower than using pandas' vectorized `pd.to_timedelta` and `pd.to_datetime`. Adding a `timedelta` array to a `datetime` object produces a `DatetimeIndex`, so `.strftime()` must be called directly on it without the `.dt` accessor.
**Action:** Always prefer pandas vectorized operations for large-scale synthetic timestamp generation to drastically reduce execution time.
