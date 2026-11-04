## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-18 - Redundant Pandas DataFrame filtering in Streamlit rendering
**Learning:** In Streamlit apps, repeatedly filtering a Pandas DataFrame (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both metric calculation and rendering causes duplicate $O(N)$ operations which are evaluated on every re-render.
**Action:** Extract the filtered DataFrame into a variable and reuse it. This halves the filtering overhead and improves application responsiveness.
