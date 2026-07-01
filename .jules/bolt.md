## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-02 - Redundant Streamlit DataFrame Filtering
**Learning:** Recalculating the same DataFrame filter multiple times (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for metrics and later for rendering causes redundant execution on every UI interaction in Streamlit.
**Action:** Always assign filtered DataFrames to variables early in the script and reuse them for both metrics calculations and UI rendering to save processing time.
