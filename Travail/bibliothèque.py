livres = {}

def menu():
    print('''===== Menu =====
1 - Ajouter un livre
2 - Afficher tous les livres
3 - Rechercher un livre
4 - Supprimer un livre
5 - Quitter
''')
    
def option1():
    titre = input("Entrez le titre : ")
    auteur = input("Entrez l'auteur titre : ")
    try:
        date = int(input("Entrez l'année de publication : "))
    except ValueError:
        print("La date ne peut etre en lettre")
    livres[titre] = {"auteur": auteur, "date": date}
    print(f'✅ Livre "{titre}" ajouté avec succès !')

def option2():
    for livre, infos in livres.items():
        print("📚 Liste des livres :")
        print(f"- {livre}, {infos['auteur']} {infos['date']}")

        

def option3():
    titre = input("Entrez le titre à rechercher : ")
    if titre in livres:
        print(f'✅ Livre trouvé : {titre}, {livres[titre]["auteur"]} ({livres[titre]["date"]})')
    else:
        print("Le livre est introuvable")

def option4():
    titre = input("Entrez le titre à supprimer : ")
    if titre in livres.items():
      del livres[titre]
      print(f'✅ Livre "{titre}" supprimé avec succès !')
    else:
     print("Le livre est inexistant")

while True:
    menu()
    user = input("Choisissez une option : ")
    if user == "1":
        option1()
    elif user == "2":
        option2()
    elif user == "3":
        option3()
    elif user == "4":
        option4()
    elif user == "5":
        print("👋 Au revoir !")
        break
    else:
       print("Option inexistant, veuillez réesayer")