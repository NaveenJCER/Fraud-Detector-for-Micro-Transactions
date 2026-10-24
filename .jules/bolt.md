## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2026-10-24 - Redundant Pandas DataFrame filtering in Streamlit
**Learning:** In Streamlit applications where metrics and data tables require the same filtered view, re-evaluating the mask on the DataFrame causes duplicate work.
**Action:** Hoist the filter expression to a variable and reuse it for both metric calculations and UI rendering.
