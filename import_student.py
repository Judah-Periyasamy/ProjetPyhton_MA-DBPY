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

def get_class(id):
    query = "SELECT firstname, lastname FROM students WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    row = cursor.fetchone()
    cursor.close()
    return row



open_dbconnection()
with open(filename_classes, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=(";"))
    next(csvreader, None)
    for row in csvreader:
        add_classes(row[0],row[1])

close_dbconnection()