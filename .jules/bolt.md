## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-24 - Streamlit Redundant DataFrame Filtering
**Learning:** Redundant pandas DataFrame filtering (e.g., repeated calls to `df[df['anomaly_flag'] == 'Fraud']`) causes unnecessary re-evaluation. Since Streamlit runs top-to-bottom on every interaction, these redundant operations block the main thread, whereas caching the filtered subset in a variable can achieve >2x performance speedup.
**Action:** Always compute filtered DataFrames once and reuse the variable for subsequent metrics and rendering calls in Streamlit scripts.
