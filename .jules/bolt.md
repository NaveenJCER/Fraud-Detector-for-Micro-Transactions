## 2024-03-02 - [Streamlit redundant filtering]
**Learning:** In Streamlit, the entire script re-runs on every user interaction, making redundant memory allocations and CPU cycles costly. The previous code was doing redundant DataFrame filtering.
**Action:** Avoid redundant DataFrame filtering by storing the filtered result in a variable and reusing it for metric calculation and display to minimize memory allocations and CPU cycles.
