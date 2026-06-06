## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Streamlit redundant DataFrame filtering
**Learning:** In Streamlit apps, recalculating the same pandas DataFrame filter (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for multiple components (metrics vs. displaying the table) causes unnecessary redundant processing, doubling the execution time for that specific operation.
**Action:** Always filter the DataFrame once, cache it in a variable, and reuse the subset for both metrics (using `len()`) and rendering to achieve a >2x speedup on filtering operations.
