import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

# Load the dataset
df = pd.read_csv("data/transactions.csv")

# Select numeric features for model
X = df[["amount"]].copy()

# Optional normalization (scaling)
X["amount"] = np.log1p(X["amount"])  # log scale for better results

# Build Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.02,  # approx 2% anomalies expected
    random_state=42,
)

# Fit the model
model.fit(X)

# ⚡ Bolt Optimization:
# IsolationForest.predict() calls decision_function() internally.
# By calculating the score once and deriving predictions manually,
# we skip the redundant internal call, halving inference time.
score = model.decision_function(X)
df["anomaly_flag"] = np.where(score < 0, -1, 1)
df["fraud_score"] = score

# Convert -1 to 'Fraud', 1 to 'Legit'
df["anomaly_flag"] = df["anomaly_flag"].map({1: "Legit", -1: "Fraud"})

# Save the model
joblib.dump(model, "model/fraud_model.pkl")

# Save results with predictions
df.to_csv("data/scored_transactions.csv", index=False)

print("✅ Model training complete!")
print("💾 Saved model to model/fraud_model.pkl")
print("📊 Scored data saved to data/scored_transactions.csv")
print(df.head(10))
