## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-02 - Redundant Pandas Filtering in UI Apps
**Learning:** In Streamlit apps (like `fraud-detector/app/app.py`), repeatedly filtering a pandas DataFrame for the same condition (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both metrics calculation and data rendering creates unnecessary overhead.
**Action:** Cache the filtered subset in a variable and reuse it across the application to achieve measurable >2x performance speedup.
