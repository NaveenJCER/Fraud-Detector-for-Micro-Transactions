## 2024-05-24 - Isolation Forest Inference Optimization
**Learning:** Calling `predict(X)` and `decision_function(X)` on scikit-learn's IsolationForest performs redundant tree traversals, duplicating the inference cost.
**Action:** Always compute `decision_function(X)` once and use `np.where(score < 0, -1, 1)` to derive predictions manually when both scores and labels are needed.

## 2024-05-24 - Streamlit Filtering Optimization
**Learning:** Redundant DataFrame filtering in Streamlit applications (e.g., calculating metrics and visualizing the same subset) causes unnecessary memory allocations and CPU cycles on every re-render.
**Action:** Always store the filtered result in a variable and reuse it for metrics, visualizations, and conditions to minimize overhead.
