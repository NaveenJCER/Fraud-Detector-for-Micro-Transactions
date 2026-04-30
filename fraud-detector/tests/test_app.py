import sys
import os
import unittest
from unittest.mock import MagicMock
import importlib
import pandas as pd

# Mock dependencies before importing app.py
mock_st = MagicMock()
mock_st.columns.return_value = [MagicMock(), MagicMock(), MagicMock()]
# Make cache_data a pass-through decorator
mock_st.cache_data = lambda func: func
sys.modules['streamlit'] = mock_st

mock_px = MagicMock()
sys.modules['plotly.express'] = mock_px

# Ensure we can import app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestApp(unittest.TestCase):
    def setUp(self):
        # Create a sample dataframe
        self.sample_df = pd.DataFrame({
            'transaction_id': ['TXN1', 'TXN2', 'TXN3'],
            'amount': [100.0, 5000.0, 200.0],
            'anomaly_flag': ['Legit', 'Fraud', 'Legit'],
            'fraud_score': [1.0, -1.5, 0.5]
        })

        # Mock pd.read_csv to return the sample dataframe
        self.original_read_csv = pd.read_csv
        pd.read_csv = MagicMock(return_value=self.sample_df)

        # Reset streamlit mocks
        mock_st.reset_mock()
        mock_st.columns.return_value = [MagicMock(), MagicMock(), MagicMock()]

    def tearDown(self):
        pd.read_csv = self.original_read_csv

    def test_app_logic(self):
        # Import (or reload) app to trigger top-level execution
        if 'app.app' in sys.modules:
            app = importlib.reload(sys.modules['app.app'])
        else:
            from app import app

        # Verify the calculations made in app.py
        self.assertEqual(app.total_txns, 3)
        self.assertEqual(app.fraud_txns, 1)
        self.assertEqual(app.legit_txns, 2)

        # Verify frauds dataframe was computed correctly
        self.assertEqual(len(app.frauds), 1)
        self.assertEqual(app.frauds.iloc[0]['transaction_id'], 'TXN2')

if __name__ == '__main__':
    unittest.main()
