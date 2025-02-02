from data_collector import DataFetcher
from database_manager import DatabaseManager

def main():
    # Define database credentials
    db_config = {
        "db_name": "stock_data",
        "db_user": "dmajeti",  # Replace with PostgreSQL username
        "db_password": "Sairam_202412",  # Replace with PostgreSQL password
        "db_host": "localhost",
        "db_port": "5432",
    }

    # Initialize database manager
    db_manager = DatabaseManager(**db_config)

    # Define tickers
    tickers = ["TCS.BO", "RELIANCE.BO", "INFY.BO"]

    # Initialize data fetcher
    fetcher = DataFetcher(tickers)

    # Fetch data
    metadata = fetcher.fetch_metadata()
    #historical_data = fetcher.fetch_historical_data()
    #intraday_data = fetcher.fetch_intraday_data()
    #corporate_actions = fetcher.fetch_corporate_actions()
    #financials = fetcher.fetch_financials()

    # Print the fetched data
    print(metadata)

    # Store data in the database
    db_manager.insert_data("stocks", metadata)
    #db_manager.insert_data("historical_data", historical_data)
    #db_manager.insert_data("intraday_data", intraday_data)
    #db_manager.insert_data("corporate_actions", corporate_actions)
    #db_manager.insert_data("financials", financials)

    # Close the database connection
    db_manager.close_connection()

if __name__ == "__main__":
    main()
