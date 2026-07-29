## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2025-05-24 - Streamlit Redundant DataFrame Filtering
**Learning:** In Streamlit apps that load large datasets into memory, redundantly filtering a Pandas DataFrame (e.g., `df[df['flag'] == 'X']`) to calculate metrics and then again to display a table causes significant performance overhead, doubling the filtering cost.
**Action:** Always cache the filtered subset in a variable (e.g., `filtered_df = df[...]`) and reuse it for metrics (`len(filtered_df)`) and rendering (`st.dataframe(filtered_df)`) to optimize execution speed.
