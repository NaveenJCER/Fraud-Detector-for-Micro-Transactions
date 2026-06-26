## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2026-06-26 - Streamlit redundant dataframe filtering
**Learning:** In Streamlit apps, redundant pandas DataFrame filtering causes unnecessary CPU overhead. However, when refactoring to cache the subset, UI rendering calls like `st.subheader` must not be inadvertently moved, as they dictate the sequential rendering layout.
**Action:** Always cache filtered subsets early, but maintain the exact order of Streamlit UI calls to preserve the dashboard's visual layout.
