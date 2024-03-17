import psycopg2
from psycopg2 import OperationalError
from functions import *

# connect to postgres db
connection = create_connection(
    "postgres", "postgres", "marvin", "127.0.0.1", "5432"
)

#drop previous database
#god_function(connection, "DROP DATABASE comp3005a3")

#create database 
god_function(connection, "CREATE DATABASE COMP3005A3")

#now connect to the database
connection = create_connection(
  "comp3005a3", "postgres", "marvin", "127.0.0.1", "5432"
)

#create tables
create_tables = """
CREATE TABLE students(
	student_id SERIAL,
	first_name VARCHAR(25) NOT NULL,
	last_name VARCHAR(25) NOT NULL,
	email VARCHAR(30) UNIQUE NOT NULL,
	enrollment_date DATE,
	Primary Key (student_id)
);
"""
file_query(connection, create_tables)

#insert base data
base_data = """
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
"""
file_query(connection, base_data)


# function definitions

#function for getting all entries in the student table
def getAllStudents():
    #generate query to be used (select everything from table and order ascending)
    get_all = """
    SELECT * FROM public.students
    ORDER BY student_id ASC 
    """

    #call printable_query function that returns cursor.fetchall() so that we can print the result of the query
    try:
        result = printable_query(connection, get_all)
    except:
        print("getAllStudents() query failed")
    
    #iterate on the result of the query and print out each column + the values for the column
    for row in result:
        print("student_id =", row[0])
        print("first_name =", row[1])
        print("last_name =", row[2])
        print("email =", row[3])
        print("enrollment_date =", row[4], "\n")

#function for adding student into the database
def addStudent(first_name, last_name, email, enrollment_date):

    #query for inserting data based on params added
    query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('" + first_name + "', '" + last_name + "', '" + email + "', '" + enrollment_date + "');"
    #file the query using predefined function
    try:
        file_query(connection, query)
    except:
        print("addStudent query function failed to execute")

#function for updating student email that has the corresponding student id
def updateStudentEmail(student_id, new_email):

    #generate query to be used (update where the student id is the same)
    query = "UPDATE students SET email = '" + new_email + "' WHERE student_id = " + str(student_id) + ";"

    #file query using predefined function
    try:
        file_query(connection, query)
    except:
        print("updateStudentEmail failed")

#function for deleting a row from the DB corresponding to a specific student id
def deleteStudent(student_id):

    #generate query to be used (delete row where student id is the same as param)
    query = "DELETE FROM students WHERE student_id = " + str(student_id) + ";"

    #file query using predefined function
    try:
        file_query(connection, query)
    except:
        print("delete student failed")

#define main functions
def main():

    print("using function getALLStudents() : \n")
    getAllStudents()

    input ("=== press enter to commence the next part of the application demonstration ===")
    
    print("== adding student to DB, getting info from user == \n\n")
    first_name = input("please input the first name of the student you would like to add: ")
    last_name = input("please input the first name of the student you would like to add: ")
    email = input("please input the email of the student you would like to add: ")
    enrollment_date = input("please input the enrollment date of the student you would like to add: ")

    print("inserting data into student table using user inputs and addStudent(): \n\n")

    addStudent(first_name, last_name, email, enrollment_date)

    print("displaying updated Table: \n\n")

    getAllStudents()

    input ("=== press enter to commence the next part of the application demonstration ===")

    print("modifying student 1's email, changing value to butt_licker@hotmail.com: \n\n")

    updateStudentEmail(1, "butt_licker@hotmail.com")

    getAllStudents()

    input ("=== press enter to commence the next part of the application demonstration ===")

    print("== DELETING A ROW FROM DB, GETTING USER INPUT ==")

    student_id = input("input student id of student you wish to delete from DB: ")

    print("deleting input student from database using deleteStudent(): \n")

    deleteStudent(student_id)

    print("displaying updated Table: \n\n")

    getAllStudents()

    print("thanks for using my application! :)")

#execute main function
main()
