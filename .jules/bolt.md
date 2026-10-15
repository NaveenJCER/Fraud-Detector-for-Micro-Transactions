## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2026-10-15 - Cache Streamlit DataFrame Filters
**Learning:** Repeatedly filtering pandas DataFrames (e.g., df[df['col'] == 'val']) in Streamlit scripts for both metric calculation and rendering duplicates work.
**Action:** Always cache the filtered subset in a variable and reuse it across the script to halve evaluation time.
