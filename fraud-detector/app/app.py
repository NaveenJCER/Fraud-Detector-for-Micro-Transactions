import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# Page setup
st.set_page_config(page_title="Fraud Detector Dashboard", layout="wide")

st.title("💳 Fraud Detector for Micro-Transactions")
st.markdown("This dashboard displays flagged suspicious transactions detected by the Isolation Forest model.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/scored_transactions.csv")
    return df

df = load_data()

# Summary metrics
total_txns = len(df)
fraud_txns = len(df[df['anomaly_flag'] == 'Fraud'])
legit_txns = total_txns - fraud_txns

# Display summary
col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", total_txns)
col2.metric("Fraudulent", fraud_txns)
col3.metric("Legit", legit_txns)

st.markdown("---")

# Show fraud transactions
st.subheader("⚠️ Flagged Fraudulent Transactions")
frauds = df[df['anomaly_flag'] == 'Fraud']

if frauds.empty:
    st.info("No suspicious transactions detected ✅")
else:
    st.dataframe(frauds, use_container_width=True)

# Visualization
st.markdown("---")
st.subheader("📊 Transaction Amount Distribution")

fig = px.histogram(df, x="amount", color="anomaly_flag",
                   title="Distribution of Transaction Amounts",
                   nbins=30, barmode='overlay')
st.plotly_chart(fig, use_container_width=True)

# Optional: Fraud score visualization
st.subheader("🔍 Fraud Score Analysis")
fig2 = px.scatter(df, x="transaction_id", y="fraud_score", color="anomaly_flag",
                  title="Fraud Score by Transaction")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.caption("Developed by Team – 24 Hour Hackathon Project 💻")
