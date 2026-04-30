## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-02 - Streamlit offline testing caching pitfalls
**Learning:** When using `MagicMock` to offline test Streamlit components, decorators like `@st.cache_data` will return a mock object instead of executing the wrapped function. This causes subsequent data processing logic (e.g. `len(df)`) to fail (returning 0) because the mock object itself is evaluated rather than the returned dataframe.
**Action:** When mocking `streamlit` for offline unit tests, explicitly mock decorators like `cache_data` as pass-through functions (e.g., `mock_st.cache_data = lambda func: func`) to ensure the underlying logic executes and returns the correct data.
