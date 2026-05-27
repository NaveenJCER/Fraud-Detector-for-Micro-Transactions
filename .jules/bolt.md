## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Streamlit Redundant Filtering Overhead
**Learning:** In Streamlit apps, the entire script reruns top-to-bottom on every interaction. Performing identical DataFrame filtering multiple times across different UI sections compounds overhead linearly per re-render.
**Action:** Always compute filtered subsets once and reuse the cached variable for all subsequent metrics and UI components to minimize render time.
