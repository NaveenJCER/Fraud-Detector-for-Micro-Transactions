## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-10-06 - Streamlit DataFrame Filtering
**Learning:** In Streamlit apps, filtering a DataFrame repeatedly (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both metrics calculation and data rendering duplicates expensive operations on every re-render.
**Action:** Cache the filtered subset in a variable and reuse it for both `len()` and rendering to reduce execution time.
