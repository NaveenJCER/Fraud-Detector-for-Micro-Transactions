## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-23 - Avoid redundant pandas filtering in Streamlit
**Learning:** Performing `df[df['anomaly_flag'] == 'Fraud']` multiple times in a Streamlit script repeats the filtering operation on every render.
**Action:** Extract the filtered subset to a variable `frauds` and reuse it for computing lengths and rendering dataframes to halve processing time.
