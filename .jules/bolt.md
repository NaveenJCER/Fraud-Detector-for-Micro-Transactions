## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Streamlit Redundant DataFrame Filtering
**Learning:** In Streamlit apps, repeated DataFrame filtering (e.g., `df[df['flag'] == 'X']`) across different sections of a script causes redundant O(N) operations on every re-render.
**Action:** Always cache filtered subsets into variables early in the script and reuse them for both metric calculations and data rendering to achieve >2x speedup on those operations.
