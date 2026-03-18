
## 2024-05-28 - Streamlit Data Filtering Optimization
**Learning:** In Streamlit applications, each user interaction causes the entire script to run top-to-bottom. Redundant DataFrame filtering (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for both metric calculations and visualization results in unnecessary memory allocations and CPU usage.
**Action:** Always store the filtered result in a variable (e.g., `frauds`) and reuse it throughout the script to minimize redundant operations.
