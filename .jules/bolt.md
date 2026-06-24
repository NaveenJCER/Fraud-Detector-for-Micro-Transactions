## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-12 - Streamlit Redundant pandas DataFrame Filtering
**Learning:** In Streamlit apps that load large datasets, repeating DataFrame filtering operations like `df[df['anomaly_flag'] == 'Fraud']` across multiple components redundantly triggers expensive Pandas evaluations and blocks the main thread.
**Action:** Always cache filtered DataFrame subsets into a variable early in the script execution, and reuse that variable for downstream metrics, aggregations, and rendering to achieve >2x execution speedup.
