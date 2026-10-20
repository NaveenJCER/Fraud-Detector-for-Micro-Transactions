## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-04-02 - Redundant DataFrame filtering in Streamlit
**Learning:** In Streamlit apps, it's common to repeatedly filter a pandas DataFrame (e.g., `df[df['condition'] == True]`) to compute summary metrics and later to render the data. This duplicates the filtering work.
**Action:** Cache the filtered subset in a variable and reuse it for both metrics and rendering to eliminate redundant operations.
