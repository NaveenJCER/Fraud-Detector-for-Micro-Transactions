## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-22 - Redundant filtering in Streamlit rendering
**Learning:** Streamlit executes the entire script on every interaction. Redundant pandas DataFrame filtering (like recalculating `df[df['anomaly_flag'] == 'Fraud']` for both metrics and tables) doubles the filtering cost on every render cycle, leading to measurable slowdowns.
**Action:** Always compute filtered DataFrame subsets once and cache them in variables before rendering UI components that share the same data subset.
