import pandas as pd
from .connector import DatabaseConnector

class DatabaseManager:
    def __init__(self):
        self.connector = DatabaseConnector()

    def save_dataframe(self, df: pd.DataFrame, table_name: str = None):
        """Save a DataFrame to the SQLite database."""
        table_name = table_name or self.connector.table_name
        with self.connector as conn:
            df.to_sql(
                name=table_name,
                con=conn,
                if_exists="replace",  # or 'append' for merges
                index=False
            )

    def read_table(self, table_name: str = None) -> pd.DataFrame:
        """Read a table from SQLite into a DataFrame."""
        table_name = table_name or self.connector.table_name
        with self.connector as conn:
            return pd.read_sql(f"SELECT * FROM {table_name}", con=conn)