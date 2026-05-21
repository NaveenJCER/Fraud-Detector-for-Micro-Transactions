## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-01 - Redundant Pandas Filtering in Streamlit
**Learning:** Redundant calls to filter a Pandas DataFrame (e.g. `df[df['flag'] == 'X']`) across multiple sections of a Streamlit app can add up. Streamlit's top-to-bottom execution means these computations are repeated every run.
**Action:** Always cache filtered subsets of DataFrames in variables and reuse them for metrics and rendering to reduce execution time.
