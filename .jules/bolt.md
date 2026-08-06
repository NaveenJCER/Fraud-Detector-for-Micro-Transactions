## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-01 - Redundant Pandas Filtering in UI
**Learning:** In Streamlit apps, redundant pandas DataFrame filtering (e.g., repeated calls to `df[df['anomaly_flag'] == 'Fraud']`) can cause measurable slowdowns during every UI re-render, especially as dataset sizes grow.
**Action:** Always filter DataFrames once, cache the resulting subset in a variable (e.g., `frauds`), and reuse it for subsequent metrics, calculations, and UI rendering to effectively halve filtering overhead.
