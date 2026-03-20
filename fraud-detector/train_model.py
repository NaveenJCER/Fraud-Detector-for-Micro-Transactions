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

# Predict anomalies
# ⚡ Bolt Optimization: Calling `predict` and `decision_function` separately
# doubles inference time. Calculate `decision_function` once and derive predictions
# manually (score < 0 indicates anomaly).
df["fraud_score"] = model.decision_function(X)

# Derive anomaly flag directly (Legit if score >= 0, Fraud if score < 0)
df["anomaly_flag"] = np.where(df["fraud_score"] < 0, "Fraud", "Legit")

# Ensure anomaly_flag precedes fraud_score as per data requirements
cols = list(df.columns)
# fraud_score and anomaly_flag are the last two columns added. Let's reorder them
# to make sure anomaly_flag is right before fraud_score, preserving order of other columns.
if "anomaly_flag" in cols and "fraud_score" in cols:
    cols.remove("anomaly_flag")
    cols.remove("fraud_score")
    df = df[cols + ["anomaly_flag", "fraud_score"]]

# Save the model
joblib.dump(model, "model/fraud_model.pkl")

# Save results with predictions
df.to_csv("data/scored_transactions.csv", index=False)

print("✅ Model training complete!")
print("💾 Saved model to model/fraud_model.pkl")
print("📊 Scored data saved to data/scored_transactions.csv")
print(df.head(10))
