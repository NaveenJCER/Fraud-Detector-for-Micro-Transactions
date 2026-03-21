## 2024-03-21 - [Isolation Forest Predict Optimization]
**Learning:** Calling `predict()` and `decision_function()` on a Scikit-Learn IsolationForest model computes the same internal tree traversals twice. In `train_model.py`, this doubles inference time.
**Action:** Always compute `decision_function()` first, then manually derive predictions using `np.where(scores < 0, -1, 1)`.

## 2024-03-21 - [Redundant DataFrame Filtering in Streamlit]
**Learning:** In Streamlit applications, filtering DataFrames multiple times for the same condition (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both metric calculation and visualization wastes memory allocations and CPU cycles.
**Action:** Always store the filtered result in a variable and reuse it for both `len()` calculations and subsequent visualizations.
