## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-24 - Streamlit sequential execution and redundant filtering
**Learning:** Streamlit evaluates the script sequentially on every interaction. Redundantly filtering pandas DataFrames (e.g., computing `df[df['anomaly_flag'] == 'Fraud']` multiple times for counts and rendering) adds unnecessary latency that scales with data size.
**Action:** Always cache filtered DataFrame subsets in variables if they are used multiple times within the same Streamlit script, while ensuring UI rendering elements (like `st.subheader`) remain in their original sequential order to prevent visual regressions.
