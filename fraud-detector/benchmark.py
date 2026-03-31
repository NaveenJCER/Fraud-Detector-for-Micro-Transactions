import time
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def benchmark_train():
    # Create large dummy dataset
    X = pd.DataFrame({'amount': np.random.uniform(50, 10000, 100000)})
    X['amount'] = np.log1p(X['amount'])

    model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
    model.fit(X)

    # Unoptimized
    t0 = time.time()
    for _ in range(10):
        a = model.predict(X)
        b = model.decision_function(X)
    t1 = time.time()

    # Optimized
    t2 = time.time()
    for _ in range(10):
        fraud_score = model.decision_function(X)
        anomaly_flag = np.where(fraud_score < 0, -1, 1)
    t3 = time.time()

    print(f"Train Model - Unoptimized: {t1-t0:.4f}s")
    print(f"Train Model - Optimized:   {t3-t2:.4f}s")

def benchmark_app():
    df = pd.DataFrame({
        'anomaly_flag': np.random.choice(['Legit', 'Fraud'], 1000000, p=[0.98, 0.02])
    })

    # Unoptimized
    t0 = time.time()
    for _ in range(100):
        fraud_txns = len(df[df['anomaly_flag'] == 'Fraud'])
        frauds = df[df['anomaly_flag'] == 'Fraud']
    t1 = time.time()

    # Optimized
    t2 = time.time()
    for _ in range(100):
        frauds = df[df['anomaly_flag'] == 'Fraud']
        fraud_txns = len(frauds)
    t3 = time.time()

    print(f"App - Unoptimized: {t1-t0:.4f}s")
    print(f"App - Optimized:   {t3-t2:.4f}s")

if __name__ == '__main__':
    benchmark_train()
    benchmark_app()