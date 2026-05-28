## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-28 - Streamlit redundant dataframe filtering
**Learning:** In Streamlit apps, it's common to filter a pandas DataFrame for metrics (e.g., `len(df[df['flag'] == 'Fraud'])`) and then filter it again later to display the data table (`frauds = df[df['flag'] == 'Fraud']`). This redundancy causes unnecessary performance overhead on every single re-render.
**Action:** Always extract and cache subset DataFrames in variables if they are used multiple times across different sections of a Streamlit app to halve the filtering overhead and improve rendering speed.
