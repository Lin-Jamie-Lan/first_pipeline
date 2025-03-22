import sqlite3
import pytest
from database.connector import DatabaseConnector  # Replace with your actual module and class name
import os

# Fixture to create a temporary SQLite database in memory

@pytest.fixture
def db_connector():
    # Use an in-memory SQLite database for testing
    db_path = ":memory:"
    yield_connector = DatabaseConnector(db_path)
    yield yield_connector
    # When a fixture uses yield, it provides a value (in your case, the DatabaseConnector instance) to the test function.
    # The test function receives this value as an argument (e.g., db_connector).
    # yield_connector.connect() -> dont need this, pause this, and do test functions now
    # Clean up after the test
    yield_connector.disconnect()

def test_connect(db_connector):
    """Test that the connect method establishes a valid connection."""
    print("showing db_path: ",db_connector.db_path)
    connection = db_connector.connect()
    assert isinstance(connection, sqlite3.Connection)  # Check if the connection is valid
    assert connection.total_changes == 0  # Ensure the connection is active


def test_disconnect(db_connector):
    """Test that the disconnect method closes the connection."""
    connection = db_connector.connect()
    assert isinstance(connection, sqlite3.Connection)  # Ensure connection is open
    if connection.total_changes == 0:
        print('Linnie connected')
    db_connector.disconnect()
    assert db_connector.conn is None  # Ensure connection is closed

def test_context_manager(db_connector):
    """Test that the context manager works as expected."""
    with db_connector as connection:
        assert isinstance(connection, sqlite3.Connection)  # Ensure connection is valid
        assert connection.total_changes == 0  # Ensure the connection is active
    # After exiting the context manager, the connection should be closed
    assert db_connector.conn is None


def test_table(db_connector):
    connection=db_connector.connect()
    cursor = connection.cursor()
    cursor.execute("select * from sample;")
    result = cursor.fetchone()
    print(result)
    assert True
