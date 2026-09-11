## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-24 - Redundant Pandas Filtering in Streamlit
**Learning:** Streamlit apps rerun from top to bottom on every interaction. Repeating identical pandas DataFrame filtering operations (like `df[df['anomaly_flag'] == 'Fraud']`) for metrics and UI components duplicates expensive data manipulation, causing unnecessary slowdowns in render times.
**Action:** Always cache the filtered DataFrame subset in a variable (e.g., `frauds = df[...]`) and reuse it across the script to halve the filtering overhead and speed up the app rendering by >2x.
