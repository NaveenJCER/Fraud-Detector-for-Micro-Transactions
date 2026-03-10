import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import time

# Create dummy data
X = pd.DataFrame({'amount': np.random.rand(100000)})

model = IsolationForest(
    n_estimators=100,
    contamination=0.02,
    random_state=42
)
model.fit(X)

start = time.time()
for _ in range(10):
    a = model.predict(X)
    b = model.decision_function(X)
print(f"Original: {time.time() - start:.4f}s")

start = time.time()
for _ in range(10):
    b = model.decision_function(X)
    a = np.where(b < 0, -1, 1)
print(f"Optimized: {time.time() - start:.4f}s")
