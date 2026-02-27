import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib


def main():
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

    # Performance Optimization: Calculate decision_function once and derive predictions.
    # Calling predict(X) internally calls decision_function(X), so calling both doubles the
    # computational cost. By deriving predictions manually (score < 0 is anomaly), we avoid
    # a second tree traversal, speeding up inference by ~50%.
    df["fraud_score"] = model.decision_function(X)

    # Derive anomaly_flag directly from fraud_score
    # score < 0 => anomaly (-1), score >= 0 => normal (1)
    df["anomaly_flag"] = np.where(df["fraud_score"] < 0, -1, 1)

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


if __name__ == "__main__":
    main()
