## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-04-02 - Streamlit DataFrame Filtering Redundancy
**Learning:** In Streamlit apps, it's common to filter a DataFrame to compute metrics and then filter it again later to render a table or chart. This redundant filtering forces pandas to scan the entire dataset multiple times on every re-render.
**Action:** Always store the filtered subset in a variable (e.g., `frauds = df[df['anomaly_flag'] == 'Fraud']`) and reuse it for both metrics and rendering to save processing time.
