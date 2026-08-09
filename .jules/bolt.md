## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.

## 2024-04-02 - Streamlit Pandas DataFrame Redundant Filtering
**Learning:** Recalculating the same filtered DataFrame subset (e.g. `df[df['flag'] == 'value']`) repeatedly in a Streamlit script is a common performance anti-pattern. Because Streamlit runs top-to-bottom on every interaction, these O(N) operations pile up.
**Action:** Always cache the initial filtered DataFrame in a variable (`subset = df[...]`) and reuse it for computing metrics like `len(subset)` or rendering UI components, preventing redundant full-pass evaluations.
