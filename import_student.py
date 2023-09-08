"""
MA-DBPY : Python + DB
Title: Projet Python Ordre de classe
Author : Judah Periyasamy
Version : 1.0
"""
import mysql.connector
import csv

filename_classes = "classes.csv"
filename_students = "students.csv"

def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='judah', password='Jukuporter392.', database='classroom_cleaning',
                                   buffered=True, autocommit=True)

def close_dbconnection():
    db_connection.close()


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



open_dbconnection()
with open(filename_classes, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=(";"))
    next(csvreader, None)
    for row in csvreader:
        add_classes(row[0],row[1])

close_dbconnection()

open_dbconnection()
with open(filename_students, 'r') as csvfile:
    csvreader1 = csv.reader(csvfile, delimiter=(";"))
    next(csvreader1, None)
    for row in csvreader1:
        classes_id = get_class_id(row[3])
        if classes_id == None:
            print("FAUX")
        add_student(row[0], row[1], row[2], classes_id[0])

close_dbconnection()