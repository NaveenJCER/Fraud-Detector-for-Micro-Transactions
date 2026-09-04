## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-09-04 - Redundant pandas DataFrame filtering in Streamlit
**Learning:** In Streamlit apps, recalculating the same pandas DataFrame subsets (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both metrics display and later data rendering causes redundant evaluation. Since Streamlit re-runs top-to-bottom on interaction, this redundancy compounds.
**Action:** Always filter the DataFrame once, cache the resulting subset in a variable, and reuse it for both metrics and rendering to achieve a measurable speedup.
