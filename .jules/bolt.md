## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-17 - Redundant pandas filtering in Streamlit
**Learning:** In Streamlit dashboards where variables are sequentially rendered (e.g., summary metrics followed by detailed tables), pandas DataFrames are frequently filtered multiple times for the same condition (e.g., `df[df['anomaly_flag'] == 'Fraud']`). This causes redundant iterations over the entire dataset.
**Action:** Always filter DataFrames once, cache the resulting subset in a variable, and reuse it for both metric aggregations (`len(frauds)`) and downstream visualization to achieve measurable performance gains (>2x speedup on the filtering step).
