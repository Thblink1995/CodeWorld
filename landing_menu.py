import misc as m


def start(ng):
    m.clear()
    print("bienvenue dans code World !")
    save_key = choixPseudo(ng)  #IMPORTANT ici on récupère la clé de sauvegarde
    print(
        "Félicitation voyageur du code, apprêtez-vous à entrer dans Code World !"
    )
    m.clear()
    return save_key



def choixPseudo(ng) -> str:
    if ng == "1":  #le joueur n'a jamais joué, on crée une save avec son pseudo (scénario normal)
        rep = ' '
        while rep != "oui":
            perso = input("choisissez le nom de votre personnage : \n")
            print(f"\nVoulez-vous être : {perso}?")
            rep = input("\noui/non :\n")
        #création d'une sauvegarde:
        dic_save[perso] = {"personnage": perso}
        m.export_file("save", dic_save)
        choixClasse(perso)
        return perso
    if ng == "2":  #le joueur a déjà un pseudo et cherche à reprendre sa progression (scénario complexe)
        print("\nQuel était votre pseudo ? \n")
        #ICI, bug à régler, on est coincé dans la boucle si y a pas déjà de save existante (ligne 144)
        liste = list(dic_save.keys())
        for i in range(len(liste)):  #on affiche une liste de numéros avec les save déjà existantes
            print(f"{i+1} : {liste[i]}")
        perso = input("\n pseudo : ")

        if perso.isnumeric() != True or not 0 < int(perso) <= len(liste):
            choixPseudo("2")
        else:
            rep = liste[int(perso) - 1]
        #transférer le joueur directement à la progression associé au pseudo
    #-------------------------
    return rep


def choixClasse(save_key):
    """
    debut : save_key est le nom du joueur actuel
    fin : retourne la classe choisie et verifiée du joueur (save_key)
    """
    print("\nchoisissez votre classe :")
    for i in classesdico:
        print(i)
    classep = str(input("\nclasse : \n"))
    #si ce que met le joueur n'est ni mage ni guerrier :
    verifPossibleClasse(classep, save_key)
    return None


def verifPossibleClasse(classep, save_key):
    """
    entrée :
        classep -> str -> la classe choisie à vérifier
        save_key -> str -> clé de sauvegarde (nom joueur)
    fct :
        vérifie que le joueur a bien choisi une classe existante
    sortie :
        None
    """
    while classep != classes_key[0] and classep != classes_key[1]:
        print("\nécrire une classe existante.")
        for i in classesdico:
            print(i)
        classep = str(input("classe : \n"))
    verifClasse(classep, save_key)
    return None

def verifClasse(classep, save_key):
    """
    Entrée : sécurise/confirme le choix du joueur avec oui/non\n
        classedico -> dic -> dictionnaire qui contient toutes les classes et leurs specs
    Fin :

    """
    print(f"\nVoulez-vous être un {classep} ?")
    rep = str(input("oui / non : \n"))
    if rep != "oui":
        #retourne au choix de la classe
        choixClasse(save_key)
    else:
        #stockage du choix dans la save

        dic_save[save_key]["classe"] = classep
        dic_save[save_key]["emplacement"] = "/PC/overworld/batch/auberge_CodeX"
        dic_save[save_key]["progression"] = "0"
        #définit l'inventaire du joueur en fonction de sa classe
        if classep == "mage":
            dic_save[save_key]["inventaire"] = "0,3,4"
        elif classep == "guerrier":
            dic_save[save_key]["inventaire"] = "0,1,2"
    HP = classesdico[classep]["HP"]
    dic_save[save_key]["HP"] = HP
    m.export_file("save",dic_save)


    return None