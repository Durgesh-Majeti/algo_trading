import yfinance as yf
import pandas as pd
from datetime import datetime

class DataFetcher:
    def __init__(self, tickers):
        self.tickers = tickers

    def fetch_metadata(self):
        """Fetch metadata for tickers."""
        print("Fetching metadata...")
        metadata = []
        for ticker in self.tickers:
            stock = yf.Ticker(ticker)
            info = stock.info
            metadata.append({
                "ticker": ticker,
                "company_name": info.get("longName"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
                "isin": info.get("isin", ""),
                "exchange": info.get("exchange"),
                "currency": info.get("currency"),
                "created_at": datetime.now(),
            })
        return pd.DataFrame(metadata)

    def fetch_historical_data(self, start_date="2010-01-01", end_date=None):
        """Fetch historical data for tickers."""
        print("Fetching historical data...")
        historical_data = []
        end_date = end_date or datetime.now().strftime("%Y-%m-%d")
        
        for ticker in self.tickers:
            stock = yf.Ticker(ticker)
            hist = stock.history(start=start_date, end=end_date)
            for index, row in hist.iterrows():
                historical_data.append({
                    "ticker": ticker,
                    "date": index.date(),
                    "open_price": row["Open"],
                    "high_price": row["High"],
                    "low_price": row["Low"],
                    "close_price": row["Close"],
                    "volume": row["Volume"],
                    "adjusted_close": row["Close"],  # Adjusted close is assumed as Close
                    "created_at": datetime.now(),
                })
        return pd.DataFrame(historical_data)

    def fetch_intraday_data(self):
        """Fetch intraday data for tickers."""
        print("Fetching intraday data...")
        intraday_data = []
        for ticker in self.tickers:
            stock = yf.Ticker(ticker)
            intraday = stock.history(period="1d", interval="5m")
            for index, row in intraday.iterrows():
                intraday_data.append({
                    "ticker": ticker,
                    "timestamp": index,
                    "price": row["Close"],
                    "volume": row["Volume"],
                    "created_at": datetime.now(),
                })
        return pd.DataFrame(intraday_data)

    def fetch_corporate_actions(self):
        """Mock corporate actions data."""
        print("Fetching corporate actions (mock data)...")
        corporate_actions = []
        for ticker in self.tickers:
            corporate_actions.append({
                "ticker": ticker,
                "action_type": "Dividend",
                "action_date": "2023-03-31",
                "value": 10.0,  # Mock value
                "created_at": datetime.now(),
            })
        return pd.DataFrame(corporate_actions)

    def fetch_financials(self):
        """Mock financials data."""
        print("Fetching financials (mock data)...")
        financials = []
        for ticker in self.tickers:
            financials.append({
                "ticker": ticker,
                "year": 2023,
                "revenue": 1000000.0,  # Mock data
                "net_profit": 200000.0,  # Mock data
                "eps": 50.0,  # Mock data
                "created_at": datetime.now(),
            })
        return pd.DataFrame(financials)
