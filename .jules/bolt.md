## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-08 - Redundant pandas filtering in Streamlit
**Learning:** Streamlit renders UI elements sequentially and reruns the entire script on interaction. Redundant DataFrame filtering (e.g., `df[df['anomaly_flag'] == 'Fraud']`) multiple times in the script causes the expensive operation to repeat on every re-render.
**Action:** Cache filtered subsets of DataFrames in variables and reuse them for metrics and visualization to achieve significant (>2x) performance speedups.
