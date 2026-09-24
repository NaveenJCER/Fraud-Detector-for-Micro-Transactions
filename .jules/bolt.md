## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-24 - Streamlit Pandas Filtering Redundancy
**Learning:** In Streamlit apps, repeatedly filtering pandas DataFrames (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for calculating summary metrics and later for rendering the data duplicates work and slows down re-renders.
**Action:** Always cache the filtered subset in a variable early on and reuse it for both metrics calculations and subsequent UI rendering to reduce unnecessary re-computation in every render cycle.
