## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-06-22 - Streamlit Top-to-Bottom Execution Data Bottleneck
**Learning:** Streamlit re-evaluates the entire script top-to-bottom on every user interaction. Redundant pandas DataFrame filtering (e.g., calculating the same subset multiple times for different metrics/views) becomes a compounding performance bottleneck, forcing the app to repeat expensive data operations on every render cycle.
**Action:** Always cache filtered DataFrames or expensive intermediate variable states into variables if they are used multiple times in a Streamlit script to ensure operations run only once per render cycle.
