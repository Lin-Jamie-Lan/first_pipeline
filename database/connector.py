import os
import sqlite3
from typing import Optional

class DatabaseConnector:
    def __init__(self):
        self.db_path = os.getenv("SQLITE_DB_PATH")
        self.table_name = os.getenv("SQLITE_TABLE_NAME")
        self.conn: Optional[sqlite3.Connection] = None

# SQLite configuration
# export SQLITE_DB_PATH="$HOME/my_databases/pipeline_data.db"
# export SQLITE_TABLE_NAME="processed_data"


    def connect(self) -> sqlite3.Connection:
        """Connect to SQLite database."""
        if not self.conn:
            self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def disconnect(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()