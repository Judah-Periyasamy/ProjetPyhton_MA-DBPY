"""
MA-DBPY : Python + DB
Title: Projet Python Ordre de classe
Author : Judah Periyasamy
Version : 1.0
"""
import mysql.connector

def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='judah', password='Jukuporter392.', database='classroom_cleaning',
                                   buffered=True, autocommit=True)
    return db_connection
def close_dbconnection():
    db_connection.close()

def get_class_info(class_name):
    cursor = db_connection.cursor()
    query = "SELECT id, name, room from classes where name = %s"
    cursor.execute(query, (class_name,))
    row = cursor.fetchone()
    cursor.close()
    return row

def delete_student(user_input, user_input2, user_input3):
    query = "DELETE FROM students WHERE lastname = %s AND firstname = %s and class_id = (select id from classes where name = %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (user_input, user_input2, user_input3))
    affected_rows = cursor.rowcount
    cursor.close()
    if affected_rows == 1:
        return True
    else:
        return False

def add_student(lastname, firstname, student_email, classname):
    class_info = get_class_info(classname)
    if class_info is None:
        raise Exception('Erreur dans le nom de la classe, vérifiez-le.')
    else:
        cursor = db_connection.cursor()
        # first column is the id of the class
        class_id = class_info[0]
        query = "insert into students (lastname, firstname, email, class_id) values (%s, %s, %s, %s)"
        cursor.execute(query, (lastname, firstname, student_email, class_id))
        affected_rows = cursor.rowcount
        cursor.close()
        if affected_rows == 1:
            return True
        else:
            return False

def get_student_info(user_input,user_input2):
    query = "SELECT firstname, lastname FROM classes WHERE lastname = %s and firstname = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (user_input,user_input2))
    row = cursor.fetchone()
    cursor.close()
    return row

def get_index_student(lst, value):
    """
    get the position of the searched element (student) in the list
    :param lst: the list in which we want to search
    :param value: the value we search
    :return: the position of the value in the list
    """
    pos = 0
    for elt in lst:
        if elt[0] == value:
            return pos
        else:
            pos += 1
    return pos