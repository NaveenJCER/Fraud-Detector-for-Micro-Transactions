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

# Predict anomalies (-1 = anomaly, 1 = normal)
# OPTIMIZATION: Predict re-calculates decision_function. calculate decision_function once and derive predictions.
# Scores < 0 are anomalies (-1), scores >= 0 are normal (1).
df['fraud_score'] = model.decision_function(X)
df['anomaly_flag'] = np.where(df['fraud_score'] < 0, 'Fraud', 'Legit')

# Reorder columns to match original output (anomaly_flag before fraud_score)
cols = df.columns.tolist()
if cols[-1] == 'anomaly_flag' and cols[-2] == 'fraud_score':
    cols[-1], cols[-2] = cols[-2], cols[-1]
    df = df[cols]

# Save the model
joblib.dump(model, "model/fraud_model.pkl")

# Save results with predictions
df.to_csv("data/scored_transactions.csv", index=False)

print("✅ Model training complete!")
print("💾 Saved model to model/fraud_model.pkl")
print("📊 Scored data saved to data/scored_transactions.csv")
print(df.head(10))
