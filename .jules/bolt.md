## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-07 - Redundant pandas DataFrame filtering
**Learning:** Calling `df[df['column'] == 'value']` multiple times is an expensive O(N) operation. We discovered this in Streamlit apps where UI rendering loops execute top-level code on each interaction.
**Action:** Always assign the filtered subset of a DataFrame to a variable (e.g., `filtered_df = df[...]`) when it needs to be reused for metrics (like `len()`) or display components, cutting execution time in half.
