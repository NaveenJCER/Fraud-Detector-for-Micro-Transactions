## 2024-02-28 - [Avoid Redundant DataFrame Filtering]
**Learning:** In pandas and Streamlit applications, repeatedly filtering a DataFrame with the same condition (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for multiple operations like row counts and creating subsets can introduce an architectural bottleneck, unnecessarily recalculating boolean masks, allocating extra memory, and slowing down render speeds.
**Action:** Always store filtered DataFrames in a temporary variable and reuse that variable across multiple operations.
