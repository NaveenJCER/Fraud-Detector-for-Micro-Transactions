## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-24 - Redundant DataFrame filtering in Streamlit
**Learning:** Redundant pandas DataFrame filtering (e.g., repeated `df[df['col'] == 'val']`) in Streamlit scripts causes unnecessary re-evaluations during every render cycle.
**Action:** Cache the filtered subset in a variable and reuse it for downstream metrics and rendering to achieve measurable >2x performance speedup.
