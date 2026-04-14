## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-19 - Streamlit Redundant Filtering
**Learning:** In Streamlit apps displaying data summaries, identical DataFrame filters (e.g., `df[df['flag'] == True]`) are often evaluated repeatedly across different metric definitions and rendering steps.
**Action:** Always extract common DataFrame filters into single variables at the top level of the Streamlit script, significantly reducing memory and CPU overhead while keeping rendering calls sequential.
