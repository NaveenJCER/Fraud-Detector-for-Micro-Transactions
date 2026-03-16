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

# Predict anomalies (-1 = anomaly, 1 = normal)
# ⚡ Bolt Optimization: Calculate decision_function once and derive predictions
# to avoid duplicate tree traversal in predict(X), halving inference time.
df["fraud_score"] = model.decision_function(X)
df["anomaly_flag"] = np.where(df["fraud_score"] < 0, -1, 1)

# Convert -1 to 'Fraud', 1 to 'Legit'
df["anomaly_flag"] = df["anomaly_flag"].map({1: "Legit", -1: "Fraud"})

# ⚠️ train_model.py outputs a serialized model to model/fraud_model.pkl and a CSV to data/scored_transactions.csv.
# The script explicitly enforces column ordering so that anomaly_flag precedes fraud_score to maintain compatibility.
# Reorder columns to ensure anomaly_flag comes before fraud_score
cols = df.columns.tolist()
cols.remove("fraud_score")
cols.remove("anomaly_flag")
cols.extend(["anomaly_flag", "fraud_score"])
df = df[cols]

# Save the model
joblib.dump(model, "model/fraud_model.pkl")

# Save results with predictions
df.to_csv("data/scored_transactions.csv", index=False)

print("✅ Model training complete!")
print("💾 Saved model to model/fraud_model.pkl")
print("📊 Scored data saved to data/scored_transactions.csv")
print(df.head(10))
