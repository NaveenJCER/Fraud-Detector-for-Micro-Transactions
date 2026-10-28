## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-24 - Streamlit Pandas Filtering Optimization
**Learning:** Repeatedly filtering pandas DataFrames (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both metrics and rendering in Streamlit duplicates work and degrades performance on larger datasets.
**Action:** Always extract and cache the filtered subset in a variable before using it for multiple metrics or UI components.
