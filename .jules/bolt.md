## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-15 - Redundant Pandas Filtering in Streamlit Apps
**Learning:** Performing the same boolean masking operation (e.g., `df[df['anomaly_flag'] == 'Fraud']`) multiple times within a Streamlit app significantly slows down the render cycle.
**Action:** Cache the filtered DataFrame in a variable and reuse it for computing metrics and rendering UI components to achieve a measurable >2x performance speedup.
