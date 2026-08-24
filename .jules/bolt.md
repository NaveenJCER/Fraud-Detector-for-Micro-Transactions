## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-18 - Streamlit Redundant Pandas Filtering
**Learning:** In Streamlit apps, redundant DataFrame filtering (e.g., repeatedly calling `df[df['anomaly_flag'] == 'Fraud']` for metrics and table rendering) can be surprisingly expensive since the entire script re-runs on every user interaction.
**Action:** Always cache the filtered subset in a variable early on and reuse it across multiple components to achieve measurable speedups (e.g., >2x) without altering functionality.
