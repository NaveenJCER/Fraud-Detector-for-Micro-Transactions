## 2024-05-24 - [Avoid Redundant DataFrame Filtering in Streamlit]
**Learning:** In Streamlit applications, redundant DataFrame filtering (e.g., computing `df[df['anomaly_flag'] == 'Fraud']` multiple times for different metrics or visualizations) wastes memory allocations and CPU cycles, slowing down the app on every re-run.
**Action:** Always compute filtered dataframes once and store them in a variable to reuse for both metric calculation and rendering.
