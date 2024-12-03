def stream_user_ages():
    """Generator that yields user ages one by one."""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data;")
    for row in cursor:
        yield row['age']
    cursor.close()
    connection.close()

def calculate_average_age():
    """Calculates the average age using a generator."""
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    average_age = total_age / count if count > 0 else 0
    print(f"Average age of users: {average_age:.2f}")