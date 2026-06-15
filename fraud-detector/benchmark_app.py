import pandas as pd
import time
import streamlit as st

def run_current():
    df = pd.read_csv("data/scored_transactions.csv")
    total_txns = len(df)
    fraud_txns = len(df[df['anomaly_flag'] == 'Fraud'])
    legit_txns = total_txns - fraud_txns
    frauds = df[df['anomaly_flag'] == 'Fraud']
    return fraud_txns, legit_txns

def run_optimized():
    df = pd.read_csv("data/scored_transactions.csv")
    total_txns = len(df)
    frauds = df[df['anomaly_flag'] == 'Fraud']
    fraud_txns = len(frauds)
    legit_txns = total_txns - fraud_txns
    return fraud_txns, legit_txns

# Test many times to magnify
import timeit
print("Current:", timeit.timeit(run_current, number=100))
print("Optimized:", timeit.timeit(run_optimized, number=100))
