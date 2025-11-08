import pandas as pd
import numpy as np
from datetime import datetime, timedelta
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
start_date = datetime.now() - timedelta(days=30)
timestamps = [
    (start_date + timedelta(seconds=random.randint(0, 2592000))).strftime("%Y-%m-%d %H:%M:%S")
    for _ in range(num_records)
]

# Random locations (optional)
locations = random.choices(
    ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata"],
    k=num_records
)

# Random payment methods
payment_methods = random.choices(
    ["Credit Card", "Debit Card", "UPI", "NetBanking", "Wallet"],
    k=num_records
)

# Combine into DataFrame
df = pd.DataFrame({
    "transaction_id": transaction_ids,
    "user_id": user_ids,
    "amount": amounts,
    "timestamp": timestamps,
    "location": locations,
    "payment_method": payment_methods
})

# Add a few "fraud-like" transactions (randomly make 5–10 look suspicious)
fraud_indices = np.random.choice(df.index, size=10, replace=False)
df.loc[fraud_indices, "amount"] = df.loc[fraud_indices, "amount"] * np.random.uniform(5, 10)
df.loc[fraud_indices, "user_id"] = [f"U{random.randint(51, 60)}" for _ in range(10)]

# Save to CSV
df.to_csv("data/transactions.csv", index=False)

print("✅ transactions.csv generated successfully!")
print(df.head(10))
