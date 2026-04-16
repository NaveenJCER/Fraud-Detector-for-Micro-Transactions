## 2024-05-24 - Avoid `__pycache__` commits
**Learning:** Compiled Python bytecode files (`.pyc` files in `__pycache__`) should never be committed as they add redundant binary bloat, cause merge conflicts across different platforms, and violate standard version control best practices.
**Action:** Always clean the working tree of temporary and binary files (e.g., run `git status` to ensure `__pycache__` is excluded, or ensure `.gitignore` lists it) before committing, and use `git rm --cached` if they are accidentally added.

## 2024-05-24 - Explicit Comments for Optimization Directives
**Learning:** System constraints requiring explanatory comments (e.g., "Always add comments explaining the optimization") are strictly enforced in code reviews. Skipping them leads to PR rejection.
**Action:** Always add inline comments explicitly marking the optimization and explaining its intent (e.g., using `⚡ Bolt optimization:` prefix) before submitting code for review.
