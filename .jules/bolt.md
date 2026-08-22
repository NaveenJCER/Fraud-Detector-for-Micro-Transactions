## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-15 - Redundant Pandas Filtering in Streamlit
**Learning:** Performing `df[df['col'] == 'val']` multiple times in a Streamlit script re-executes the filtering on every render.
**Action:** Always extract and cache the filtered subset in a variable if it's used for multiple operations (e.g., metrics and rendering) to achieve a >2x performance speedup.
