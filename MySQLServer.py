import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",    
            user="root",         
            password="password"  
        )

        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()

            # SQL query to create the database
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)

            # Print success message
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Print error message in case of failure
        print(f"Error: {e}")

    finally:
        # Ensure the connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
