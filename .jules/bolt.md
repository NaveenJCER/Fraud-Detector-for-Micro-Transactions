## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-05-15 - Streamlit duplicate Pandas filtering overhead
**Learning:** Streamlit re-runs scripts top-to-bottom on every interaction. Doing the exact same O(N) Pandas DataFrame filtering operation twice (once for getting a count via `len(df[df['col'] == 'val'])`, and again later to display the subset via `df[df['col'] == 'val']`) effectively halves performance during that render cycle. Caching the filtered subset early and reusing it cuts this overhead entirely.
**Action:** Always scan Streamlit or UI logic for repeated data processing expressions. Assign the result to a variable first before deriving counts, metrics, or tables from it.
