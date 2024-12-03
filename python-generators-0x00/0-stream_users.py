import mysql.connector

def stream_users():
    """Generator that streams rows one by one from the user_data table."""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data;")
    for row in cursor:
        yield row
    cursor.close()
    connection.close()