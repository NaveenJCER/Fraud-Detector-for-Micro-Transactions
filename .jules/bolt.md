## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2026-06-03 - Streamlit redundant DataFrame filtering
**Learning:** Redundant pandas DataFrame filtering operations in Streamlit cause unnecessary overhead since the script re-runs entirely on interaction.
**Action:** Always compute filtered subsets once per Streamlit run and cache them in variables to reuse for both aggregate metrics and UI rendering to improve execution speed.
