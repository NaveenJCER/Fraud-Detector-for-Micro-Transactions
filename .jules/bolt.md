## 2024-04-01 - IsolationForest redundant predict() calls
**Learning:** `IsolationForest.predict(X)` internally calls `decision_function(X)` to calculate scores and map them to -1/1. If you also need `fraud_score = model.decision_function(X)`, calling both methods duplicates the expensive calculation, doubling inference time.
**Action:** Always compute `decision_function(X)` first, and derive predictions manually using `np.where(scores < 0, -1, 1)` to effectively halve inference time without changing behavior.
## 2024-05-12 - Redundant Pandas Filtering in Streamlit
**Learning:** In Streamlit apps, repeated DataFrame filtering operations (like `df[df['flag'] == 'Val']`) during sequential rendering calculations scale poorly as dataset size increases, creating measurable slow-downs on UI reload.
**Action:** Always filter the DataFrame once into a local variable and reuse that filtered subset for subsequent aggregations (like `len()`) and display logic.
