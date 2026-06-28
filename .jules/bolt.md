## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-20 - Streamlit Redundant Pandas Filtering
**Learning:** In Streamlit apps, redundant pandas DataFrame filtering (e.g. `df[df['anomaly_flag'] == 'Fraud']`) can easily happen because UI variables are calculated separately from display data. This recalculates the mask every time, degrading performance.
**Action:** Always cache the filtered subset in a variable and reuse it for both metrics calculations (like `len()`) and rendering to achieve measurable >2x performance speedup.
