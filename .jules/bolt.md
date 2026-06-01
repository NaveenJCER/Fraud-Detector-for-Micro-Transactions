## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Streamlit Redundant Filtering
**Learning:** Streamlit apps re-run top-to-bottom on every interaction. Redundant pandas DataFrame filtering (e.g., calling `df[df['anomaly_flag'] == 'Fraud']` multiple times for metrics and tables) compounds this overhead significantly.
**Action:** Always cache the filtered subset in a variable and reuse it for metrics and rendering to achieve a measurable >2x performance speedup.
