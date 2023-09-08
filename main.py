"""
MA-DBPY : Python + DB
Title: Projet Python Ordre de classe
Author : Judah Periyasamy
Version : 1.0
"""
from import_student import *
def delete_student():
    pass

def choose_menu():
    list_menu = print("""
    1. Afficher l’ordre en classe
    2. Générer le planning « Ordre en classe »
    3. Valider l’ordre en classe de la semaine
    4. Supprimer un élève de la liste
    5. Ajouter un élève de la liste
    6. Générer le document « Ordre en classe »
    7. Sortir du menu """)
    print("")
    while True:
        try:
            user_menu = int(input("Veuillez choisir un menu : "))
            while user_menu < 1 or user_menu > 7:
                print("Menu inéxistant")
                print("")
                user_menu = int(input("Veuillez choisir un menu : "))
            while user_menu == 1 or user_menu == 2 or user_menu == 3 or user_menu == 4 or user_menu == 5 or user_menu == 6:
                print("Menu pas encore fonctionnel")
                print("TEST")
                print("")
                user_menu = int(input("Veuillez choisir un menu : "))
            if user_menu == 7:
                print("Vous allez sortir du menu")
                quit()
        except ValueError:
            print("Il faut choisir un menu entre 1 et 7")
            print("TEST")
            print("")

choose_menu()

