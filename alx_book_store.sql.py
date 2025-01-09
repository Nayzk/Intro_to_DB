import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',    
            user='nayzk',         
            password='1234567890'  
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Query to create the database
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)
            print("Database 'alx_book_store' created successfully!")
            
            # Switch to the database
            cursor.execute("USE alx_book_store")
            
            # Create tables one by one
            create_authors_table = """
            CREATE TABLE IF NOT EXISTS Authors (
                author_id INT AUTO_INCREMENT PRIMARY KEY,
                author_name VARCHAR(215) NOT NULL
            );
            """
            cursor.execute(create_authors_table)
            
            create_books_table = """
            CREATE TABLE IF NOT EXISTS Books (
                book_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(130) NOT NULL,
                author_id INT,
                price DOUBLE NOT NULL,
                publication_date DATE,
                FOREIGN KEY (author_id) REFERENCES Authors(author_id)
            );
            """
            cursor.execute(create_books_table)
            
            create_customers_table = """
            CREATE TABLE IF NOT EXISTS Customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_name VARCHAR(215) NOT NULL,
                email VARCHAR(215) NOT NULL,
                address TEXT
            );
            """
            cursor.execute(create_customers_table)
            
            create_orders_table = """
            CREATE TABLE IF NOT EXISTS Orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT,
                order_date DATE NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            );
            """
            cursor.execute(create_orders_table)
            
            create_order_details_table = """
            CREATE TABLE IF NOT EXISTS Order_Details (
                orderdetail_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT,
                book_id INT,
                quantity DOUBLE NOT NULL,
                FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                FOREIGN KEY (book_id) REFERENCES Books(book_id)
            );
            """
            cursor.execute(create_order_details_table)
            
            print("Tables created successfully!")
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        # Ensure the connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the script
if __name__ == "__main__":
    create_database()
