import pandas as pd
import numpy as np
import random

# Set random seed for consistency
np.random.seed(42)

# Number of transactions
num_records = 500

# Generate transaction IDs
transaction_ids = [f"TXN{1000 + i}" for i in range(num_records)]

# Generate random user IDs
user_ids = [f"U{random.randint(1, 50)}" for _ in range(num_records)]

# Generate random transaction amounts (₹50 – ₹10,000)
amounts = np.random.uniform(50, 10000, num_records).round(2)

# Generate timestamps (past 30 days)
# ⚡ Bolt optimization: Replaced Python list comprehension and random.randint
# with vectorized pandas and numpy operations.
# Expected impact: ~3x faster timestamp generation for large datasets.
SECONDS_IN_30_DAYS = 30 * 24 * 60 * 60
start_date_pd = pd.Timestamp.now() - pd.Timedelta(days=30)
random_seconds = np.random.randint(0, SECONDS_IN_30_DAYS, num_records)
timestamps = (
    (start_date_pd + pd.to_timedelta(random_seconds, unit="s"))
    .strftime("%Y-%m-%d %H:%M:%S")
    .tolist()
)

# Random locations (optional)
locations = random.choices(
    ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata"],
    k=num_records,
)

# Random payment methods
payment_methods = random.choices(
    ["Credit Card", "Debit Card", "UPI", "NetBanking", "Wallet"], k=num_records
)

# Combine into DataFrame
df = pd.DataFrame(
    {
        "transaction_id": transaction_ids,
        "user_id": user_ids,
        "amount": amounts,
        "timestamp": timestamps,
        "location": locations,
        "payment_method": payment_methods,
    }
)

# Add a few "fraud-like" transactions (randomly make 5–10 look suspicious)
fraud_indices = np.random.choice(df.index, size=10, replace=False)
df.loc[fraud_indices, "amount"] = df.loc[fraud_indices, "amount"] * np.random.uniform(
    5, 10
)
df.loc[fraud_indices, "user_id"] = [f"U{random.randint(51, 60)}" for _ in range(10)]

# Save to CSV
df.to_csv("data/transactions.csv", index=False)

print("✅ transactions.csv generated successfully!")
print(df.head(10))
