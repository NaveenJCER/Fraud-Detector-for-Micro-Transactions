import sys
import time
from unittest.mock import MagicMock
import pandas as pd

# Mock joblib
sys.modules['joblib'] = MagicMock()

# Mock plotly and plotly.express
mock_plotly = MagicMock()
sys.modules['plotly'] = mock_plotly
sys.modules['plotly.express'] = mock_plotly.express

# Mock streamlit
mock_st = MagicMock()
mock_st.cache_data = lambda func: func
mock_st.columns.return_value = (MagicMock(), MagicMock(), MagicMock())
sys.modules['streamlit'] = mock_st

# Create an in-memory DataFrame
dummy_df = pd.DataFrame({
    'amount': [100.0, 200.0] * 50000,
    'anomaly_flag': ['Legit', 'Fraud'] * 50000,
    'transaction_id': [f'TXN{i}' for i in range(100000)],
    'fraud_score': [1.0, -1.0] * 50000
})
pd.read_csv = lambda x: dummy_df

sys.path.append('fraud-detector/app')

start = time.time()
import app
end = time.time()

print(f"App executed in {end - start:.4f} seconds")
