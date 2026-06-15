import pandas as pd
import numpy as np

num_records = 100000
scores = np.random.uniform(-1, 1, num_records)

def method_current():
    df = pd.DataFrame()
    df["anomaly_flag"] = np.where(scores < 0, -1, 1)
    df["anomaly_flag"] = df["anomaly_flag"].map({1: "Legit", -1: "Fraud"})
    return df

def method_string():
    df = pd.DataFrame()
    # Direct mapping using np.where
    df["anomaly_flag"] = np.where(scores < 0, "Fraud", "Legit")
    return df

import timeit
print("Current mapping:", timeit.timeit(method_current, number=100))
print("Direct string mapping:", timeit.timeit(method_string, number=100))
