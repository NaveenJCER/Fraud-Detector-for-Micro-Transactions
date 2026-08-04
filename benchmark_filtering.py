import pandas as pd
import numpy as np
import timeit

# Generate mock data
df = pd.DataFrame({
    'anomaly_flag': np.random.choice(['Fraud', 'Legit'], size=100000, p=[0.02, 0.98])
})

def redundant_filter():
    fraud_txns = len(df[df['anomaly_flag'] == 'Fraud'])
    frauds = df[df['anomaly_flag'] == 'Fraud']
    return fraud_txns, frauds

def cached_filter():
    frauds = df[df['anomaly_flag'] == 'Fraud']
    fraud_txns = len(frauds)
    return fraud_txns, frauds

# Run benchmark
redundant_time = timeit.timeit(redundant_filter, number=100)
cached_time = timeit.timeit(cached_filter, number=100)

print(f"Redundant filtering time: {redundant_time:.4f}s")
print(f"Cached filtering time: {cached_time:.4f}s")
print(f"Speedup: {redundant_time / cached_time:.2f}x")
