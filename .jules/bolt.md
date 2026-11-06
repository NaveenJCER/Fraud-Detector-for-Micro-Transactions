## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2026-11-06 - Streamlit Data Filtering Redundancy
**Learning:** Streamlit's top-down execution model often encourages duplicate data filtering since variables are scoped locally to UI sections.
**Action:** When building Streamlit dashboards, pull data filtering operations up to the top level and cache the subsets in variables to reuse across multiple UI components.
