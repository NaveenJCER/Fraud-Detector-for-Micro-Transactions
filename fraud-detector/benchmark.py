import pandas as pd
import time
import numpy as np

# Create large dummy dataset
df = pd.DataFrame({
    'anomaly_flag': np.random.choice(['Fraud', 'Legit'], size=1000000, p=[0.05, 0.95]),
    'amount': np.random.rand(1000000) * 100
})

# Approach 1: Duplicate filtering
start = time.time()
fraud_txns_1 = len(df[df['anomaly_flag'] == 'Fraud'])
frauds_1 = df[df['anomaly_flag'] == 'Fraud']
time_dup = time.time() - start

# Approach 2: Cached filtering
start = time.time()
frauds_2 = df[df['anomaly_flag'] == 'Fraud']
fraud_txns_2 = len(frauds_2)
time_cached = time.time() - start

print(f"Duplicate filtering time: {time_dup:.4f}s")
print(f"Cached filtering time: {time_cached:.4f}s")
print(f"Speedup: {time_dup/time_cached:.2f}x")
