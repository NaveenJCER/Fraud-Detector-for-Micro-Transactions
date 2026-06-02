## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-06-02 - Redundant DataFrame Filtering in Streamlit
**Learning:** In Streamlit apps that re-run from top to bottom on every interaction, performing the same DataFrame filtering operation (e.g., `df[df['anomaly_flag'] == 'Fraud']`) multiple times causes unnecessary re-computation and slows down rendering.
**Action:** Cache the filtered subset in a variable the first time it is needed and reuse that variable for subsequent metrics and rendering calls to achieve measurable speedups.
