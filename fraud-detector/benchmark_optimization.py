import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import time


def benchmark_optimization():
    print("🚀 Starting benchmark...")

    # Generate dummy data
    np.random.seed(42)
    # Use larger dataset to make difference more noticeable
    X = pd.DataFrame(np.random.randn(50000, 5), columns=[f"col_{i}" for i in range(5)])

    # Train model
    print("Training model...")
    model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
    model.fit(X)
    print("Model trained.")

    # Method 1: Original (predict + decision_function)
    start_time = time.time()
    for _ in range(5):
        _ = model.predict(X)
        _ = model.decision_function(X)
    end_time = time.time()
    duration1 = end_time - start_time
    print(f"Original method duration (5 runs): {duration1:.4f}s")

    # Method 2: Optimized (decision_function + derived predict)
    start_time = time.time()
    for _ in range(5):
        score2 = model.decision_function(X)
        # Verify logic: predict returns -1 for anomalies, 1 for normal
        # decision_function < 0 is anomaly
        _ = np.where(score2 < 0, -1, 1)
    end_time = time.time()
    duration2 = end_time - start_time
    print(f"Optimized method duration (5 runs): {duration2:.4f}s")

    improvement = (duration1 - duration2) / duration1 * 100
    print(f"⚡ Improvement: {improvement:.2f}%")

    # Verify correctness
    pred_original = model.predict(X)
    score_original = model.decision_function(X)

    pred_derived = np.where(score_original < 0, -1, 1)

    if np.array_equal(pred_original, pred_derived):
        print("✅ Outputs match perfectly!")
    else:
        print("❌ Outputs do NOT match!")
        print("Mismatches:", np.sum(pred_original != pred_derived))


if __name__ == "__main__":
    benchmark_optimization()
