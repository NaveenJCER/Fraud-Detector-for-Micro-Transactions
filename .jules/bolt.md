## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Caching pandas DataFrame filtering in Streamlit apps
**Learning:** In Streamlit apps, redundant pandas DataFrame filtering operations (e.g., repeating `df[df['anomaly_flag'] == 'Fraud']` for metrics and rendering) cause unnecessary overhead and slow down rendering on each interaction.
**Action:** Always cache the filtered subset in a variable and reuse it for metrics and rendering to achieve a measurable >2x performance speedup on the filtering operation.
