## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-10 - Duplicate DataFrame filtering in Streamlit
**Learning:** In Streamlit, it is easy to accidentally duplicate work by filtering the same DataFrame for different components (metrics vs data tables) in different parts of the script.
**Action:** Always extract and cache filtered sub-DataFrames into variables early in the script and reuse them to eliminate redundant O(N) operations.
