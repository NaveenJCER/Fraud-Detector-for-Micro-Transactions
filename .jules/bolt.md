## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-26 - Pandas Redundant Filtering in Streamlit Apps
**Learning:** In Streamlit apps (like `fraud-detector/app/app.py`), filtering pandas DataFrames repeatedly (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for metrics and display is redundant and slows down rendering.
**Action:** Always cache the filtered subset in a variable and reuse it for metrics, rendering, and other calculations to achieve a measurable speedup (e.g., >2x for this operation).
