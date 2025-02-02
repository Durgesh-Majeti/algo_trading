import psycopg2
from sqlalchemy import create_engine

class DatabaseManager:
    def __init__(self, db_name, db_user, db_password, db_host, db_port="5432"):
        self.engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
        self.connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )

    def insert_data(self, table_name, data):
        """Insert data into a specified table."""
        try:
            data.to_sql(table_name, con=self.engine, if_exists="append", index=False)
            print(f"Data inserted into {table_name} successfully!")
        except Exception as e:
            print(f"Error inserting data into {table_name}: {e}")

    def get_stock_id(self, ticker):
        """Get stock ID from the 'stocks' table."""
        query = f"SELECT stock_id FROM stocks WHERE ticker = '{ticker}'"
        result = self.engine.execute(query).fetchone()
        return result[0] if result else None

    def close_connection(self):
        """Close the database connection."""
        self.connection.close()
        print("Database connection closed.")
