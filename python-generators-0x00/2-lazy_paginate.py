def lazy_paginate(page_size):
    """Fetches paginated data lazily from the user_data table."""
    offset = 0
    while True:
        rows = paginate_users(page_size, offset)
        if not rows:
            break
        yield rows
        offset += page_size

def paginate_users(page_size, offset):
    """Fetches a specific page of data."""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset};")
    rows = cursor.fetchall()
    connection.close()
    return rows
