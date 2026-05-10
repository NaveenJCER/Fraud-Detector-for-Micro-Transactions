## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-10 - Redundant Pandas Filtering in Streamlit
**Learning:** Redundant pandas DataFrame filtering (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for calculating both counts and subsets in Streamlit apps causes measurable slowdowns on every render.
**Action:** Always filter the DataFrame once, cache the result in a variable, and reuse it for metrics (`len(subset)`) and rendering. This avoids duplicate operations and can result in a >2x speedup.
