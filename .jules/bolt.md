## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Streamlit Redundant DataFrame Filtering
**Learning:** In Streamlit apps like `app.py`, performing the same DataFrame filtering operation (e.g., `df[df['anomaly_flag'] == 'Fraud']`) multiple times causes redundant computations on every script re-run, doubling the execution time of that logic.
**Action:** Always cache the filtered subset in a variable and reuse it for both metrics and rendering to achieve measurable >2x performance speedup on the filtering operation.
