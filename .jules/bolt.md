## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-02 - Redundant Pandas Filtering in Streamlit
**Learning:** Repeating boolean indexing on DataFrames (like `df[df['flag'] == 'X']`) in Streamlit apps for both metrics calculation and rendering wastes processing time, causing >2x slower execution since it runs on every component interaction.
**Action:** Cache the filtered DataFrame in a variable and reuse it for both metric aggregations and rendering to avoid O(n) re-computation.
