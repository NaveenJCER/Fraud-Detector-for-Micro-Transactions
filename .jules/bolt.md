## 2024-03-08 - Reusing Filtered DataFrames in Streamlit
**Learning:** Redundant DataFrame filtering operations (e.g., `df[df['anomaly_flag'] == 'Fraud']`) for metric calculation and visualization significantly increase memory allocation and CPU cycles, which is especially noticeable as the dataset grows.
**Action:** Always store the filtered result in a variable and reuse it for metrics and displays to minimize processing overhead.
