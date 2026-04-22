## 2024-05-24 - Streamlit Re-render Optimization
**Learning:** In Streamlit applications, DataFrame filtering is often duplicated—once for metric calculation (e.g., `len(df[condition])`) and once for display (`st.dataframe(df[condition])`). Because Streamlit reruns the entire script on interaction, these redundant operations accumulate. Extracting the filtered view to a variable (`frauds = df[condition]`) halves the filtering overhead.
**Action:** Always scan Streamlit files for duplicate DataFrame masks or filtering operations. Pre-compute and reuse these views *before* they are needed for layout metrics to ensure O(N) instead of O(2N) filtering.

## 2024-05-24 - Implicit Caching Pitfall
**Learning:** I encountered a review rejection because I inadvertently committed Python bytecode (`__pycache__`). Even pure logic optimizations can trigger side effects like compilation artifacts in the working directory when executed.
**Action:** Always clean the working directory (e.g., `rm -rf __pycache__`) and use `git status` or equivalent verifications to ensure no binary artifacts or diagnostic files are staged alongside code changes.
