## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-01 - Redundant DataFrame Filtering in Streamlit
**Learning:** In Streamlit apps, repeating the same pandas DataFrame filtering (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both metrics and rendering causes redundant computations that block the main thread and slow down UI rendering.
**Action:** Always cache filtered subsets in variables at the earliest point they are needed and reuse them across all subsequent metrics and UI elements to achieve measurable speedups (>2x).
