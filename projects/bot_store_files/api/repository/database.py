import mysql.connector 

def create_db():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='db_store_files'
        )

    except Exception as ex:
        print(f'Error: {ex}')

    return mydb