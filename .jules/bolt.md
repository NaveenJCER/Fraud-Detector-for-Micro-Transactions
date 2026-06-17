## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-01 - Redundant pandas DataFrame filtering in Streamlit
**Learning:** Streamlit apps rerun from top to bottom. Repeatedly filtering the same subset of a pandas DataFrame (e.g., `df[df['anomaly_flag'] == 'Fraud']`) recalculates the mask each time, wasting CPU cycles and slowing down the UI rendering.
**Action:** Always filter the DataFrame once and cache it in a variable for reuse across metrics, tables, and visualizations.
