## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2025-02-27 - Streamlit Duplicate Data Filtering
**Learning:** Re-filtering a pandas DataFrame multiple times for the exact same condition (e.g. `df[df['anomaly_flag'] == 'Fraud']`) for different UI components duplicates expensive operations. In Streamlit apps where the script reruns top-to-bottom on every interaction, these costs compound rapidly.
**Action:** Cache the filtered subset into a variable immediately after the initial data load, and reuse that variable for all subsequent metric calculations and rendering.
