import pandas as pd 
import numpy as np 
import psycopg2
import openpyxl

def main_db_connect():

    db_connection = psycopg2.connect( 
        host='ep-steep-rice-561755.ap-southeast-1.aws.neon.tech',
        port='5432',
        dbname='di_final_project',
        user='sebo964',
        password='cKoai9SPCp0z',
        sslmode='require'
    )
    print ("Main Database connection successful")
    return db_connection

def display_entries_in_main_db():
    db_connection = main_db_connect()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM login_databaseconnection")
    # print headers of table
    print(cursor.description)
    rows = cursor.fetchall()
    # Print each row
    for row in rows:
        print(row)


def add_new_entry(host, port, name, database, user, password):
    db_connection = main_db_connect()
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO login_databaseconnection (name, host, port, database, username, password) VALUES (%s, %s, %s, %s, %s, %s)", (name, host, port, database, user, password))
    db_connection.commit()
    cursor.close()
    db_connection.close()
    print("new user added successfully")
    

def user_db_select_and_connection(name):
    db_connections = main_db_connect()
    cursor = db_connections.cursor()
    cursor.execute(f"SELECT * FROM login_databaseconnection WHERE database = '{name}'")
    listofdicts = [dict(zip([key[0] for key in cursor.description], row)) for row in cursor.fetchall()]
    listofdicts_dicts = {}
    for i in listofdicts:
        listofdicts_dicts.update(i)
    return listofdicts_dicts
    
    

def connect_user_db(listofdicts):
    
    host = listofdicts['host']
    port = listofdicts['port']
    name = listofdicts['database']
    user= listofdicts['username']
    password = listofdicts['password']
    db_user_connection = psycopg2.connect( 
        host=host,
        port=port,
        dbname=name,
        user=user,
        password=password,
    )
    print ("User Database connection successful")
    return db_user_connection

def get_schemas(db_user_connection):
    cursor = db_user_connection.cursor()
    cursor.execute("SELECT schema_name FROM information_schema.schemata")
    schemas = cursor.fetchall()
    print(schemas)
    return schemas

def get_tables(db_user_connection, schema):
    cursor = db_user_connection.cursor()
    cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{schema}'")
    tables = cursor.fetchall()
    print(tables)
    return tables

def show_table(db_user_connection, schema, table):
    cursor = db_user_connection.cursor()
    # schema = input("Enter schema name: ")
    # table = input("Enter table name: ")
    cursor.execute(f"SELECT * FROM {schema}.{table}")
    table = cursor.fetchall()
    df = pd.DataFrame(table)
    table_headers = df.head()
    print (table_headers)
    return table_headers

def export_to_excel (db_user_connection, schema, table):
    cursor = db_user_connection.cursor()
    cursor.execute("SELECT * FROM {}.{}".format(schema, table))
    table = cursor.fetchall()
    df = pd.DataFrame(table)
    df.to_excel( 'table.xlsx', sheet_name='table', index=False)
    

def main_program():
    print ("Main database connected")
    print ("select action to perform")
    print ("1. Add new database connection")
    print ("2. Connect to database")
    print ("3. Exit")
    action = input("Enter action number: ")
    if action == "1":
        host = input("Enter host: ")
        port = input("Enter port: ")
        name = input("Enter name: ")
        database = input("Enter database: ")
        user = input("Enter user: ")
        password = input("Enter password: ")
        add_new_entry(host, port, name, database, user, password)
    elif action == "2":
        display_entries_in_main_db()
        name = input("Enter database name: ")
        db_to_connect = user_db_select_and_connection(name)
        print(db_to_connect)
        db_user_connection = connect_user_db(db_to_connect)
        print ("Database connected")
        print ("select action to perform")
        print ("1. Show schemas")
        print ("2. Exit")
        action = input("Enter action number: ")
        if action == "1":
            get_schemas(db_user_connection)
            schema = input("Enter schema name: ")
            get_tables(db_user_connection, schema)
            table = input("Enter table name: ")
            show_table(db_user_connection, schema, table)
            print ("do you want to export to excel?")
            if input("Enter y/n: ") == "y":
                export_to_excel(db_user_connection, schema, table)
            else:
                exit()   
        elif action == "2":
            print ("Exiting")
            exit()
        else:
            print ("Invalid action")
            main_program()
    elif action == "3":
        print ("Exiting")
        exit()
    else:
        print ("Invalid action")
        main_program()
    
main_program()