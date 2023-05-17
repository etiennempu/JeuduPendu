import random
#Pour plus d'information sur le jeu lire le README.md

#Ce sous programme ouvre le fichier mots_pendu.txt lit les mots qu'il contient et en retourne un de manièere aléatoire
def selectionner_mot():
    #Sélectionne un mot aléatoire à partir du fichier texte mots_pendu.txt
    with open("mots_pendu.txt", "r") as f:
        mots = f.readlines()
        return random.choice(mots).strip()

#Cette sous fonction est la fonction de jeu
def jouer():
    print("Pour plus d'information sur le jeu lire le README.md")
    #on récupère le mot a deviné
    mot = selectionner_mot()
    lettres_devinees = set()
    lettres_mauvaises = set()
    chances = 6
    # le jeu continue tant qu'il nous reste des vie
    while chances > 0:
        etat_actuel = ""
        #on parcour le mot
        for lettre in mot:
            #si la lettre a été deviné on l'ajout a l'état actuel
            if lettre in lettres_devinees:
                etat_actuel += lettre + " "
            #sinon on ajoute "_ "
            else:
                etat_actuel += "_ "
        #on affiche l'état actuel et le nombre de chances réstante
        print(etat_actuel)
        print("Chances restantes : ", chances)

        lettre = " "
        # dans cette boucle on demande à l'utilisateur de donné une lettre et on vérifie qu'elle est bien minuscule et sans accent
        while 96 > ord(lettre) or ord(lettre) > 123:
            lettre = input("Veuillez entrer une lettre minuscule sans accent : ")
            if len(lettre) > 1 or len(lettre) == 0:
                lettre = " "
            elif lettre in lettres_devinees:
                print("tu as déjà trouvé cette lettre")
                lettre = " "
            elif lettre in lettres_mauvaises:
                print("tu t'es déjà trompé avec cette lettre...")
                lettre = " "

        #si la lettre est contenue dans le mot on l'ajoute à la liste des mettres deviné
        if lettre in mot:
            lettres_devinees.add(lettre)
            print("La lettre est dans le mot.")
        #sinon on enlève 1 chance
        else:
            chances -= 1
            lettres_mauvaises.add(lettre)
            print("La lettre n'est pas dans le mot.")

        #condition de vitctoire toutes les lettres du mot on été trouvé on informe le joueur et on quitte
        if all(lettre in lettres_devinees for lettre in mot):
            print("Vous avez gagné ! Le mot était :", mot)
            return
    #si on est sortie du while on informe le joueur de ca défaite
    print("Vous avez perdu. Le mot était :", mot)

#appelle de la fonction de jeu
jouer()
