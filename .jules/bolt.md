## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2023-11-10 - Streamlit Duplicate DataFrame Filtering
**Learning:** In Streamlit apps, repeatedly filtering pandas DataFrames (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both summary metrics and rendering the dataset re-executes the filter operation unnecessarily on every UI interaction.
**Action:** Cache the filtered DataFrame subset in a variable first, and reuse it for computing counts (via `len()`) and rendering in the UI to save processing overhead.
