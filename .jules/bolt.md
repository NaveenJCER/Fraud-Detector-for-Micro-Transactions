## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-09 - Caching repeated DataFrame operations in Streamlit
**Learning:** Streamlit apps re-run from top-to-bottom on every interaction. If expensive operations (like filtering a large DataFrame: `df[df['anomaly_flag'] == 'Fraud']`) are repeated multiple times (e.g. for calculating metrics and again for rendering a table), this incurs unnecessary computational overhead on every render cycle.
**Action:** Always assign the result of expensive filtering operations to a variable (e.g., `frauds = df[...]`) when first needed, and reuse that variable for subsequent calculations (e.g., `len(frauds)`) and UI rendering calls.
