import mysql.connector
import pymysql as MySQLdb

def create_db():
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='db_store_files'
        )

    except Exception as ex:
        print(f'Error: {ex}')

    return db


def fetch_products():
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='db_store_files'
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT name, price, category FROM products")
    
    products = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return products
