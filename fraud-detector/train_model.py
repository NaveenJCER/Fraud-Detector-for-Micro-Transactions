import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

# Load the dataset
df = pd.read_csv("data/transactions.csv")

# Select numeric features for model
X = df[['amount']].copy()

# Optional normalization (scaling)
X['amount'] = np.log1p(X['amount'])  # log scale for better results

# Build Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.02,  # approx 2% anomalies expected
    random_state=42
)

# Fit the model
model.fit(X)

# Predict anomalies
# Optimization: Calculate fraud score first. predict() calls decision_function internally
# and thresholds it. By manually thresholding, we avoid re-computing the decision tree paths.
df['fraud_score'] = model.decision_function(X)
df['anomaly_flag'] = np.where(df['fraud_score'] < 0, 'Fraud', 'Legit')

# Save the model
joblib.dump(model, "model/fraud_model.pkl")

# Reorder columns to match original output (anomaly_flag before fraud_score)
# This ensures downstream consumers (and tests) see the exact same CSV structure.
cols = [c for c in df.columns if c not in ['anomaly_flag', 'fraud_score']]
cols += ['anomaly_flag', 'fraud_score']
df = df[cols]

# Save results with predictions
df.to_csv("data/scored_transactions.csv", index=False)

print("✅ Model training complete!")
print("💾 Saved model to model/fraud_model.pkl")
print("📊 Scored data saved to data/scored_transactions.csv")
print(df.head(10))
