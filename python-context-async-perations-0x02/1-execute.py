import sqlite3

class ExecuteQuery:
    """Context manager for executing a database query with parameters."""

    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None

    def __enter__(self):
        """Establish a database connection and execute the query."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params or [])
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
