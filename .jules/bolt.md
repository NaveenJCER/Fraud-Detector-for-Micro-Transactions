## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-03 - Streamlit redundant DataFrame filtering
**Learning:** In Streamlit apps, redundant pandas filtering operations (e.g., `len(df[df['flag'] == 'Fraud'])` and later `frauds = df[df['flag'] == 'Fraud']`) recalculate the same mask multiple times.
**Action:** Cache the filtered DataFrame in a variable and reuse it for lengths and rendering to halve the time spent on filtering without changing behavior.
