## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Redundant Pandas DataFrame filtering
**Learning:** Evaluating the same boolean mask multiple times on a pandas DataFrame (e.g., `df[df['anomaly_flag'] == 'Fraud']`) incurs unnecessary O(n) overhead, especially noticeable in top-to-bottom frameworks like Streamlit.
**Action:** Always cache the filtered DataFrame subset in a variable and reuse it for subsequent metrics and rendering to achieve >2x performance speedup on those operations.
