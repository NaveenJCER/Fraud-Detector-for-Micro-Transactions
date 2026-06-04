## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-01 - Redundant DataFrame filtering in Streamlit
**Learning:** Streamlit apps run sequentially, and repeated pandas DataFrame filtering (like `df[df['anomaly_flag'] == 'Fraud']`) evaluates multiple times per render, slowing down the UI.
**Action:** Cache the filtered DataFrame subset in a variable early in the script and reuse it for computing metrics and rendering, yielding measurable performance speedup.
