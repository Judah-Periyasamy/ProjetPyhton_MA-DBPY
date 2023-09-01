"""
MA-DBPY : Python + DB
Title: Projet Python Ordre de classe
Author : Judah Periyasamy
Version : 1.0
"""

print("""
1. Afficher l’ordre en classe
2. Générer le planning « Ordre en classe »
3. Valider l’ordre en classe de la semaine
4. Supprimer un élève de la liste
5. Ajouter un élève de la liste
6. Générer le document « Ordre en classe »
7. Sortir du menu """)

def choose_menu():
    user = int(input("Veuillez choisir u n menu : "))