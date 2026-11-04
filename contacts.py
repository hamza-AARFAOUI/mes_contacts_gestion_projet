def menu():
    print("Menu")
    print("1.Ajouter un contact")
    print("2.Afficher les contacts")
    print("3.Supprimer un contact")
    print("4.Quiter")

def contacts_events():
    while True:
        menu()
        try:

                choix=int(input("choisir entre 1 et 4 "))
                if choix == 1:
                    ajouter()
                elif choix == 2:
                    afficher()
                elif choix == 3:
                     supprimer()
                elif choix == 4:
                    print("Merci d'avoir utilisé notre application Monsieur/Madame ")
                    print("! Au revoir !")
                    exit()
                else:
                    #Si le utrs écrit autre chose  #
                    print("Choix invalide  Monsieur/Madame! ")
                    print(" Veuillez choisir entre 1 et 4. ")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre !")


def ajouter():
    nom=input("Entrez le nom :").strip()
    telephone=input("Entrez le telephone :").strip()
    email=input("Entrez l'E-mail :").strip()

    taille_avant = len(mes_contacts)
    if nom != "" and telephone != "" and email != "":
        if len(mes_contacts) == 0:
            id = 1
        else:
            id = max(contact['id'] for contact in mes_contacts) + 1

        new_contact = { "id":id,"nom": nom, "telephone": telephone, "email": email}
        mes_contacts.append(new_contact)
        enregister()
        print("Contact ajouté avec succès  et bien enregister")
    else:
        print("Erreur : L'un des champs est vide.    attention!!!!")

    if taille_avant == len(mes_contacts):
        print("Erreur : Le contact n'a pas été ajouté !!!!!!!! (-_-)")




def afficher():
    if len(mes_contacts) != 0:
        print(" --LISTE DE TOUS LES CONTACTS-- ")
        for contact in mes_contacts:
            print(f" Id :{contact['id']}, | Nom :{contact['nom']} |"
                  f" Telephone :{contact['telephone']} | E-mail :{contact['email']} ")
    else:
            print("rien de contact ")


def supprimer():
    try:
        if len(mes_contacts)!=0:
             id = int(input("Entrez le Id de la personne que vous souhaitez supprimer : "))
             c_trouve = False
             for contact in mes_contacts:
                     if id == contact['id']:
                            c_trouve = True
                            mes_contacts.remove(contact)
                            enregister()
                            print("Contact est bien supprimé")
                            break
             if not c_trouve:
                     print("Ce Id d n'existe pas  pour le supprimer!")
        else:
            print("Aucun contact exist ")

    except ValueError:
        print("Erreur : veuillez saisir un Id valide !")

def enregister():
    with open("contacts.txt","w",encoding="utf-8") as file:
        print(" TESTE ....ouverture du fishier ",file.name)
        for contact in mes_contacts:
            file.write(f"{contact['id']},{contact['nom']},{contact['telephone']},{contact['email']}\n")


def contacts_ajout():
        mes_contacts2=[]

        try:
            with open("contacts.txt", "r", encoding="utf-8") as file:
                for ligne in file:
                    id, nom, telephone, email = ligne.strip().split(",")
                    contact={"id":int(id),"nom":nom,"telephone":telephone,"email":email}
                    mes_contacts2.append(contact)

        except FileNotFoundError:
            print("file n'existe pas")
        return mes_contacts2

mes_contacts=contacts_ajout()


#l'execution  des function menu()
contacts_events()
ajouter()
afficher()
supprimer()
enregister()
#

contacts_events()






