## 2024-03-15 - [Isolation Forest Predict Optimization]
 **Learning:** Calling both `predict(X)` and `decision_function(X)` on scikit-learn's Isolation Forest does redundant work since `predict(X)` essentially calls `decision_function(X)` internally.
 **Action:** Compute `decision_function(X)` once and use `np.where(scores < 0, ...)` to derive the classes, saving ~50% inference time.

## 2024-03-15 - [Streamlit Redundant DataFrame Filtering]
 **Learning:** Filtering a large DataFrame multiple times for the same condition (e.g., extracting anomalies) in a Streamlit app wastes CPU cycles and triggers redundant memory allocations on each app rerun.
 **Action:** Perform the filtering once, assign to a variable, and use that for both metric calculation (e.g. `len(frauds)`) and display logic to speed up app execution.
