import psycopg2
from psycopg2 import OperationalError

#function to establish connection to input postgreSQL database
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# function to post a query to the DB (create tables or insert data for ex)
def file_query(db, query):
    cursor = db.cursor()
    try:
        cursor.execute(query)
        db.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

#function for creating a deleting DBS (query function that omits db.commit())
def god_function(db, query):
    db.autocommit = True
    cursor = db.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")        

#function to retrieve data from DB
def printable_query(db, query):
    cursor = db.cursor()
    try:
        cursor.execute(query)
        db.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    return cursor.fetchall()


