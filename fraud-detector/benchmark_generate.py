import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
import random

num_records = 100000

def method_current():
    start_date = datetime.now() - timedelta(days=30)
    timestamps = [
        (start_date + timedelta(seconds=random.randint(0, 2592000))).strftime("%Y-%m-%d %H:%M:%S")
        for _ in range(num_records)
    ]
    return timestamps

def method_vectorized():
    start_date = pd.Timestamp.now() - pd.Timedelta(days=30)
    random_seconds = np.random.randint(0, 2592000, num_records)
    timestamps = (start_date + pd.to_timedelta(random_seconds, unit='s')).strftime("%Y-%m-%d %H:%M:%S").tolist()
    return timestamps

import timeit
print("Current:", timeit.timeit(method_current, number=10))
print("Vectorized:", timeit.timeit(method_vectorized, number=10))
