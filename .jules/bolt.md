## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-15 - Redundant Pandas Filtering in Streamlit
**Learning:** Evaluating `df[df['anomaly_flag'] == 'Fraud']` multiple times across different sections of a Streamlit app significantly increases memory usage and CPU time due to redundant boolean indexing.
**Action:** Always filter DataFrames once at the top of the data-processing block, cache the subset in a variable, and reuse it for all subsequent metrics and UI components to achieve a >2x speedup.
