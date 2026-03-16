import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import time

# Create dummy data
np.random.seed(42)
X = pd.DataFrame({'amount': np.random.uniform(50, 10000, 100000)})
X['amount'] = np.log1p(X['amount'])

model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
model.fit(X)

start = time.time()
for _ in range(10):
    pred = model.predict(X)
    score = model.decision_function(X)
print("Original time:", time.time() - start)

start = time.time()
for _ in range(10):
    score2 = model.decision_function(X)
    pred2 = np.where(score2 < 0, -1, 1)
print("Optimized time:", time.time() - start)
