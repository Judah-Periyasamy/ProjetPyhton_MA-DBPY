"""
MA-DBPY : Python + DB
Title: Projet Python Ordre de classe
Author : Judah Periyasamy
Version : 1.0
"""
import mysql.connector
import csv
from mysql.connector import errorcode

filename_classes = "classes.csv"
filename_students = "students.csv"

def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='judah', password='Jukuporter392.', database='classroom_cleaning',
                                   buffered=True, autocommit=True)
    return db_connection
def close_dbconnection():
    db_connection.close()

def delete():
    sql_delete_query1 = "TRUNCATE TABLE classroom_cleaning.classes"
    sql_delete_query2 = "TRUNCATE TABLE classroom_cleaning.students"
    cursor = db_connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    cursor.execute(sql_delete_query1)
    cursor.execute(sql_delete_query2)
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    #db_connection.commit()
    #print('number of rows deleted', cursor.rowcount)

def add_classes(classes_name, classes_room):
    query = "INSERT INTO classes (name, room) values (%s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (classes_name, classes_room))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id



def get_class_id(classe_name):
    query = "SELECT id FROM classes WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (classe_name,))
    row = cursor.fetchone()
    cursor.close()
    return row

def add_student(firstname, lastname, student_email,class_id):
    query = "INSERT INTO students (firstname, lastname, email ,class_id) values (%s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (firstname, lastname, student_email ,class_id))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id


def get_classes_from_csv():
    with open(filename_classes, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=(";"))
        next(csvreader, None)
        for row in csvreader:
            add_classes(row[0],row[1])


def get_students_from_csv():
    with open(filename_students, 'r') as csvfile:
        csvreader1 = csv.reader(csvfile, delimiter=(";"))
        next(csvreader1, None)
        for row in csvreader1:
            if len(row) != 4:
                print("il manque une colonne dans le document")
            else:
                classes_id = get_class_id(row[3])
                if classes_id == None:
                    print("Manque la classe")
                else:
                    add_student(row[0], row[1], row[2], classes_id[0])

#MAIN
try:
    open_dbconnection()
    delete()
    get_classes_from_csv()
    get_students_from_csv()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

