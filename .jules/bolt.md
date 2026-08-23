## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Pandas Redundant Filtering in Streamlit
**Learning:** Performing multiple dataframe filters on the same condition (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for metrics and display in Streamlit causes redundant computation. In large datasets, this wastes CPU cycles and memory.
**Action:** Always cache the filtered subset in a variable (e.g., `frauds = df[...]`) and reuse it for computing counts (like `len(frauds)`) and rendering to achieve >2x speedups.
