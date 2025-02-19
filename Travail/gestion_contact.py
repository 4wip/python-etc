contacts = {
    "Bob": {"numéro": "0787654321", "âge": 20},
}

def menu():
    print('''===== Menu =====
1 - Ajouter un contact
2 - Supprimer un contact
3 - Afficher tous les contacts
4 - Rechercher un contact
5 - Quitter''')

def option1():
    nom = input("Entrez le nom : ")
    numéro = input("Entrez le numéro : ")
    
    try:
        age = int(input("Entrez l'âge : ")) 
    except ValueError:
        print("Erreur : L'âge doit être un nombre !")
        return  
    
    contacts[nom] = {"numéro": numéro, "âge": age}
    print(f"Contact '{nom}' ajouté avec succès !")

def option2():
    nom = input("Entrez le nom : ")

    contacts.pop(nom)
    print(f"Contact '{nom}' retiré avec succès !")

def option3():
    print(contacts)

def option4():
    try:
        recherche = input("Recherche de nom : ")
        print(contacts[recherche])
    except KeyError:
        print("Le contact que vous cherchez n'existe pas !")

    return

while True:
    menu()
    user = input('Choisissez une option : ')
    
    if user == "1":
        option1()
    elif user == "2":
        option2()
    elif user == "3":
        option3()
    elif user == "4":
        option4()
    elif user == "5":
        print("Au revoir !")
        break  
    else:
        print("Option invalide, veuillez réessayer.")
