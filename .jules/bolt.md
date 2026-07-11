## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-24 - Streamlit redundant DataFrame filtering
**Learning:** Repeatedly filtering a pandas DataFrame in Streamlit (e.g., `df[df['flag'] == 'X']`) across multiple components causes redundant O(N) operations on every re-render.
**Action:** Cache the filtered subset in a variable once at the top of the script and reuse it for computing metrics and rendering dataframes to achieve a >2x speedup.
