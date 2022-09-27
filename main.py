import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

#Commands

create_db = """
create database Bookstore;"""

create_table_book_info = """
create table Book_Information(
Book_ID int primary key,
Title varchar(30) not null,
Genre varchar(20) not null,
Price varchar(10) not null);"""

create_table_employee_info = """
create table Employee_Information(
Employee_ID varchar(5) primary key,
Name varchar(30) not null,
Position varchar(30) not null,
Schedule varchar(30) not null,
Benefits varchar(3) not null);"""




# Callouts
connection = create_server_connection("localhost", "root", "student", "Bookstore")
execute_query(connection, create_table_employee_info)
