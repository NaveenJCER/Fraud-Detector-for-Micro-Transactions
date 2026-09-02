## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-18 - Redundant DataFrame Filtering in Streamlit
**Learning:** In Streamlit apps, redundant pandas DataFrame filtering (like repeated `df[df['anomaly_flag'] == 'Fraud']`) causes unnecessary re-evaluation during every UI interaction or re-render, creating a performance bottleneck.
**Action:** Always cache the filtered DataFrame in a variable and reuse it for metrics and component rendering to achieve measurable >2x speedups in UI responsiveness.
