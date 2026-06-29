## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-15 - Redundant dataframe filtering in Streamlit
**Learning:** In Streamlit apps, recalculating the same filtered DataFrame (like `df[df['anomaly_flag'] == 'Fraud']`) multiple times sequentially for different components (e.g., once for metrics, once for display) is an unoptimized pattern. It forces pandas to re-scan the entire dataframe unnecessarily on every app re-run.
**Action:** Always compute filtered dataframes once and cache the result in a variable (e.g., `frauds = df[...]`) before using `len(frauds)` for metrics and rendering the subset. This can provide a >2x performance speedup for those operations.
