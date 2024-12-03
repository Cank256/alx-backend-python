def stream_users_in_batches(batch_size):
    """Fetches rows in batches from the user_data table."""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) FROM user_data;")
    total_rows = cursor.fetchone()['COUNT(*)']
    for offset in range(0, total_rows, batch_size):
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset};")
        yield cursor.fetchall()
    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)