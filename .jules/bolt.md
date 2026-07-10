## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-04-02 - Streamlit Redundant DataFrame Filtering
**Learning:** Streamlit apps execute top-to-bottom on every user interaction. Redundant top-level operations like filtering dataframes (e.g., `df[df['anomaly_flag'] == 'Fraud']`) multiple times are especially costly since they run repeatedly on every UI update.
**Action:** Always filter data once, cache it in a variable, and reuse it for metrics and rendering to achieve measurable performance speedups and improve UI responsiveness.
