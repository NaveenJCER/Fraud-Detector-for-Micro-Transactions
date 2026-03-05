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

# Calculate fraud score directly
# ⚡ Bolt optimization: calculating decision_function(X) once and deriving predictions
# manually (score < 0 indicates anomaly) avoids the redundant internal call in predict(X),
# effectively halving inference time.
fraud_score = model.decision_function(X)

# Derive anomaly_flag manually (-1 = anomaly/Fraud, 1 = normal/Legit)
# Maintain column creation order: anomaly_flag then fraud_score
df["anomaly_flag"] = np.where(fraud_score < 0, "Fraud", "Legit")
df["fraud_score"] = fraud_score

# Save the model
joblib.dump(model, "model/fraud_model.pkl")

# Save results with predictions
df.to_csv("data/scored_transactions.csv", index=False)

print("✅ Model training complete!")
print("💾 Saved model to model/fraud_model.pkl")
print("📊 Scored data saved to data/scored_transactions.csv")
print(df.head(10))
