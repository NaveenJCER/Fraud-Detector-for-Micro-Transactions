## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-06-20 - Redundant Pandas DataFrame Filtering in Streamlit
**Learning:** Streamlit renders sequentially. If you filter a DataFrame for metrics (e.g., `len(df[df['condition']])`) and later filter it again for display (`df[df['condition']]`), you perform the exact same O(N) indexing operation twice.
**Action:** Always filter the DataFrame once into a variable (`subset = df[df['condition']]`), then use that variable for both `len(subset)` and subsequent UI rendering calls to halve the computation time for that subset.
