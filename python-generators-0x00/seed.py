import mysql.connector
import csv
import uuid

def connect_db():
    """Connects to the MySQL database server."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Creates the ALX_prodev database if it does not exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    print("Database ALX_prodev created successfully.")
    cursor.close()

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Creates the user_data table if it does not exist."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        );
    """)
    print("Table user_data created successfully.")
    cursor.close()

def insert_data(connection, csv_file):
    """Inserts data into the user_data table from a CSV file."""
    cursor = connection.cursor()
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            user_id = str(uuid.uuid4())
            name = row['name']
            email = row['email']
            age = row['age']
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (user_id, name, email, age))
    connection.commit()
    print(f"Data from {csv_file} inserted successfully.")
    cursor.close()
