import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_optimization_logic():
    # Setup mock data
    np.random.seed(42)
    df = pd.DataFrame({'amount': np.random.uniform(50, 10000, 100)})
    X = df[['amount']].copy()
    X['amount'] = np.log1p(X['amount'])

    model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
    model.fit(X)

    # Original logic
    orig_anomaly_flag = model.predict(X)
    orig_fraud_score = model.decision_function(X)
    orig_anomaly_flag = pd.Series(orig_anomaly_flag).map({1: 'Legit', -1: 'Fraud'})

    # Optimized logic
    scores = model.decision_function(X)
    opt_anomaly_flag = np.where(scores < 0, 'Fraud', 'Legit')
    opt_fraud_score = scores

    # Assert equivalency
    assert np.allclose(orig_fraud_score, opt_fraud_score)
    assert (orig_anomaly_flag.values == opt_anomaly_flag).all()
