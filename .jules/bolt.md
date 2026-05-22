## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-02 - Redundant pandas filtering in Streamlit
**Learning:** In Streamlit apps doing data visualization, filtering dataframes is a common operation. Repeating the exact same filter (e.g., `df[df['flag'] == 'X']`) to compute metrics and then again for displaying data doubles the computational cost.
**Action:** Always cache the filtered dataframe subset into a variable and reuse it for subsequent metrics (like `len()`) and rendering to optimize performance.
