# import mysql.connector 
import pymysql as MySQLdb

def create_db():
    try:
        db = MySQLdb.connect(
            host='localhost',port=3306,
            user='root',
            password='',
            database='db_store_files'
        )
        
        # dbparams = dict(
        #     ')
        # mydb = mysql.connector.connect(**dbparams)
        # print(mydb)

    except Exception as ex:
        print(f'Error: {ex}')

    return db
