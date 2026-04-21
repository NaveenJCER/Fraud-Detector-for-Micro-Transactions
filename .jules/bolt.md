## 2025-04-21 - Caching DataFrame filters for UI metrics
**Learning:** In Streamlit applications, repeatedly filtering DataFrames for UI display and metrics calculations introduces redundant CPU cycles and memory overhead that scale with data size.
**Action:** Always store filtered DataFrames in variables and reuse them across multiple UI components (e.g., metrics and dataframes) to avoid redundant computation.
