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

# Get fraud scores (decision function)
# Note: In IsolationForest, lower scores mean more anomalous.
# Predict calls decision_function internally, so we can save time by calling it once.
df["fraud_score"] = model.decision_function(X)

# Derive predictions: negative scores are anomalies (-1), positive are normal (1)
df["anomaly_flag"] = np.where(df["fraud_score"] < 0, "Fraud", "Legit")

# Reorder columns to match original output: anomaly_flag, then fraud_score
cols = [c for c in df.columns if c not in ["anomaly_flag", "fraud_score"]]
df = df[cols + ["anomaly_flag", "fraud_score"]]

# Save the model
joblib.dump(model, "model/fraud_model.pkl")

# Save results with predictions
df.to_csv("data/scored_transactions.csv", index=False)

print("✅ Model training complete!")
print("💾 Saved model to model/fraud_model.pkl")
print("📊 Scored data saved to data/scored_transactions.csv")
print(df.head(10))
