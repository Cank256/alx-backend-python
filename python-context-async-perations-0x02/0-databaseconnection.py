import sqlite3

class DatabaseConnection:
    """Custom context manager for handling database connections."""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """Establish a database connection."""
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
