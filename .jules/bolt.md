## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-14 - Redundant Streamlit Data Filtering
**Learning:** In Streamlit apps, because the entire script reruns on every interaction, redundant pandas DataFrame filtering (e.g., repeating `df[df['col'] == 'val']` multiple times) causes noticeable UI lag as data grows.
**Action:** Always cache the filtered subset in a variable at the top of the script and reuse it for all subsequent metrics and visualizations to achieve a >2x performance speedup.
