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

book_info = """
insert into Book_Information values
(12, "Harry Potter 1", "Fantasy", "$35.00"),
(17, "The Enemy", "Horror", "$40.00"),
(46, "House of Scorpions", "Suspense", "$31.00"),
(92, "Harry Potter 2", "Fantasy", "$39.00");"""

employee_info = """
insert into Employee_Information values
("00001", "Mark White", "CEO", "M-F, 0700-1630", "Yes"),
("00002", "Bob Blue", "Store Manager", "M-F, 0700-1630", "Yes"),
("00003", "Samuel Green", "Department Manager", "M-F, 0700-1630", "Yes"),
("00004", "Jack Violet", "Cashier", "M-F, 0700-1630", "Yes");"""

update_book = """
update Book_Information
set Price = "$100"
where Title = "Harry Potter 1";"""

delete_entry = """
delete from Book_Information
where title = "Harry Potter 2";"""

# Callouts
connection = create_server_connection("localhost", "root", "student", "Bookstore")
execute_query(connection, delete_entry)
