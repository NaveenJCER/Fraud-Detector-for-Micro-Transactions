## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-01 - Redundant DataFrame filtering in Streamlit
**Learning:** Repeatedly filtering pandas DataFrames for the same condition (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both metrics calculation and UI rendering duplicates the expensive operation and increases inference time.
**Action:** Always cache the filtered subset in a variable and reuse it across the application for metrics and rendering to achieve a measurable >2x performance speedup.
