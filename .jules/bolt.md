## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-06-27 - Streamlit redundant DataFrame filtering
**Learning:** In Streamlit apps, recalculating the same DataFrame filter multiple times (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for metrics and UI components leads to unnecessary overhead.
**Action:** Always cache the filtered subset in a variable and reuse it across metrics and rendering to avoid redundant operations and achieve measurable performance speedup.
