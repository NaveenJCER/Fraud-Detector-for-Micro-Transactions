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

# Calculate fraud score first to avoid redundant evaluations
df["fraud_score"] = model.decision_function(X)

# Predict anomalies directly from the score (<0 is anomaly)
# This avoids the redundant internal decision_function call in model.predict()
df["anomaly_flag"] = np.where(df["fraud_score"] < 0, "Fraud", "Legit")

# train_model.py output explicit enforcement of column ordering
# Ensure 'anomaly_flag' precedes 'fraud_score' to maintain compatibility
columns = [col for col in df.columns if col not in ["anomaly_flag", "fraud_score"]]
df = df[columns + ["anomaly_flag", "fraud_score"]]

# Save the model
joblib.dump(model, "model/fraud_model.pkl")

# Save results with predictions
df.to_csv("data/scored_transactions.csv", index=False)

print("✅ Model training complete!")
print("💾 Saved model to model/fraud_model.pkl")
print("📊 Scored data saved to data/scored_transactions.csv")
print(df.head(10))
