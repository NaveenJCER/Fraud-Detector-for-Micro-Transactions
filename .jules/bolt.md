## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-31 - Streamlit Redundant Dataframe Operations
**Learning:** Streamlit apps often inadvertently perform redundant O(N) operations (like dataframe filtering) because logic flows top-to-bottom and UI elements are scattered, causing the same subset to be computed multiple times for different metrics/views.
**Action:** Always cache filtered dataframes in variables high up in the script and reuse them for both calculating counts and rendering tables to cut execution time for those operations by ~50%.
