## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-08-19 - Redundant DataFrame filtering in Streamlit
**Learning:** In Streamlit apps, repeating operations like `df[df['anomaly_flag'] == 'Fraud']` across different UI components causes redundant O(N) computations on every re-render.
**Action:** Always compute the filtered dataframe once, store it in a variable, and reuse it for computing lengths (e.g., `len(frauds)`) and rendering, achieving >2x speedup for those operations.
