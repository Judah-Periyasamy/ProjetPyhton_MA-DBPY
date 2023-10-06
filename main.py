"""
MA-DBPY : Python + DB
Title: Projet Python Ordre de classe
Author : Judah Periyasamy
Version : 1.0
"""
from import_student import *
from database import *

def get_info_student():
    """
    ask the user information about the student
    :return: a dictionnary with lastname, firstname and classname the user wrote
    """
    last_name = input("Veuillez entre le nom de l'élève : ")
    first_name = input("Veuillez entre le prénom de l'élève : ")
    class_name = get_classname_student()
    return {'lastname': last_name, 'firstname': first_name, 'classname': class_name}


def get_classname_student():
    """
    ask user the classname to generate the planning
    :return: class_name
    """
    class_name = input("Veuillez entre la classe de l'élève : ")
    return class_name


def menu_info():
    print("Menu")
    print("1. Afficher l'ordre en classe")
    print("2. Générer le planning \"Ordre en classe\"")
    print("3. Valider l'ordre en classe de la semaine")
    print("4. Supprimer un élève de la liste")
    print("5. Ajouter un élève de la liste")
    print("6. Générer le document \"Ordre en classe\"")
    print("7. Sortir du menu")
    print("")

def choose_menu():
    menu_info()
    while True:
        open_dbconnection()
        try:
            user_menu = int(input("Veuillez choisir un menu : "))
            while user_menu < 1 or user_menu > 7:
                print("Menu inéxistant")
                print("")
                menu_info()
                user_menu = int(input("Veuillez choisir un menu : "))
            while user_menu == 1 or user_menu == 3 or user_menu == 6:
                print("Menu pas encore fonctionnel")
                print("")
                menu_info()
                user_menu = int(input("Veuillez choisir un menu : "))
            if user_menu == 4:
                info_student = get_info_student()
                last_name = info_student['lastname']
                first_name = info_student['firstname']
                class_name = info_student['classname']
                res = delete_student(last_name, first_name, class_name)
                if last_name == None or first_name == None or class_name == None:
                    print("Il manque une information !")
                if res:
                    print("Suppression réussie.\n")
                else:
                    print("Echec de la suppression. Assurez-vous que le nom, prénom et la classe de l'élève sont corrects.\n")
            elif user_menu == 2:
                info_student = get_info_student()
                class_name = info_student['classname']
                print(class_name)
            elif user_menu == 5:
                info_student = get_info_student()
                last_name = info_student['lastname']
                first_name = info_student['firstname']
                email = input("Veuillez entrer l'email de l'élève : ")
                class_name = info_student['classname']
                try:
                    res = add_student(last_name, first_name, email, class_name)
                    if res:
                        print("Ajout réussi.\n")
                    else:
                        print(
                            "Echec de l'ajout. Assurez-vous que le nom, prénom et la classe de l'élève sont corrects.\n")
                except Exception as exc:
                    print(exc)
                    print("")
            elif user_menu == 7:
                print("Vous allez sortir du menu")
                quit()
        except ValueError:
            print("Il faut choisir un menu entre 1 et 7")
            choose_menu()
            print("")
        menu_info()
        close_dbconnection()


choose_menu()