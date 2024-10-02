#bibliothèques-------------------------------------#
import csv
import random
import os
import time
import colorama
from colorama import Fore, Back, Style


#--------------------------------------------------#
def clearConsole():
    os.system('clear')


#ouverture de la sauvegarde------------------------#
def lit_fichier(nom_fichier: str) -> dict:
    dic_rep = {}
    #on charge le fichier et on le transforme en liste
    nom_fichier += ".csv"
    with open(nom_fichier, mode='r') as fichier_ouvert:
        tab_rep = list(csv.DictReader(fichier_ouvert, delimiter=" "))
    dic_rep = {}

    if nom_fichier == "save.csv":
        clé = "personnage"
    else :
        clé = "id"

    for i in tab_rep:
        dic_rep[i[clé]] = i
    return dic_rep


#exporter sert à actualiser les csv-----------------------
def exporter(nom_fichier: str, dic: dict) -> None:
    """
  entrée:
    nom_fichier    str    lieu d'écriture
    dic            dict   valeur à écrire
  pas de sortie, remplace ce qu'il y a dans le fichier par le dictionnaire entré
    """
    nom_colonnes = ['personnage', 'classe', 'progression', 'inventaire', 'emplacement']  #il faut mettre tous les headers dans cette liste
    fichier = open(nom_fichier + ".csv", 'w')
    with fichier:
        obj = csv.DictWriter(fichier, fieldnames=nom_colonnes, delimiter=" ")
        obj.writeheader()
        for i in dic:
            obj.writerow(dic[i])


def separateur(delimiteur: str, valeur: str) -> list:
    rep = valeur.split(delimiteur)
    return rep

def search(liste, platform) -> bool:
    """
    entrée:
      list     -> liste dans laquelle on cherche platform -> peut être une liste OU un dictionnaire;
      platform -> valeur qui est cherchée dans la liste, peut être de n'importe quel type;
    sortie:
      True/False
    """
    if type(liste) == list :
        for i in range(len(liste)):
            if liste[i] == platform:
                return True
        return False

    elif type(liste) == dict :
        clés = list(liste.keys())
        for i in range(len(clés)):
            if clés[i] == platform :
                return True
        return False

#définition des classes de personnages-------------#
guerrier = {
    "force": 10,
    "defense": 20,
    "HP": 100,
    "objet": ["coutelas", "tunique de cuir"]
}
mage = {
    "force": 5,
    "defense": 40,
    "HP": 80,
    "objet": ["bâtonnet magique", "robe déchirée"]
}
dic_classes = {"mage":mage,"guerrier":guerrier}
dic_save = lit_fichier("save")
dic_item = lit_fichier("items")
dic_mobs = lit_fichier("mobs")
classesdico = {"guerrier": guerrier, "mage": mage}
classes_values = list(classesdico.values())
classes_key = list(classesdico.keys())
dic_cmd = {
    "cd":
        "vous téléporte où vous voulez !\n   -> utilisation : cd ./ pour descendre, cd /destination pour vous déplacer",
    "pow":
        "vous montre votre position dans le système",
    "ls":
        "vous montre les chemins d'accès devant vous",
    "exit":
        "ferme le livre du Terminal",
    "autres":
        "tkt même pas"
}
map = {"/PC": {"/overworld": {"/batch": ["/auberge_CodeX", "/village"]}}}

#SETUP TERMINAL--------------------------------------------------------------
def ls(save_key: str, map: dict, visible: bool) -> list:
    """
    entrée :
      save_key -> str -> pour connaître l'emplacement du joueur
      map -> dict -> c'est juste la carte
      visible -> bool -> permet de soit print les données soit de les renvoyer
    sortie :
      rep -> list -> donne une liste des lieux accessibles par "cd"
    """
    access_path = dic_save[save_key]["emplacement"]
    liste = access_path.split("/")[1:]
    new_liste = []  #valeur temporaire
    etage = len(liste)
    for i in range(etage):  #on reprend la même liste mais en
        #remettant les "/" qui ont été enlevés par le .split()
        new_liste.append("/" + liste[i])
    liste = new_liste
    del new_liste

    tkt = map
    i = 0
    #if visible :
    #  print(f"Vous êtes à l'étage {emplacement}")
    if etage < 4 :
        for i in range(len(liste)):  #on épluche map pour ne garder que le coeur
            tkt = tkt[liste[i]]

        if visible :
            print("Vous pouvez accéder à :")
            for a in tkt :
                print(f"{a}")
    else :
        tkt = None #parcque il n'y a pas de lieux accessibles
        if visible :
            print("Il vous faut descendre pour aller ailleurs")
        pass
    if not visible :
        return tkt

def cd(save_key: str, argument: str, possibilities: list) ->None:
    """
    entrée :
      save_key -> str -> clé de la sauvegarde
      argument -> str -> ce qu'a écrit le joueur derrière "cd"
      possibilities -> list -> liste des emplacements que le joueur peut atteindre depuis sa position
    sortie :
      pas de sortie
      -> met la nouvelle position du joueur directement dans dic_save
    """
    if argument == None :
        print("il manque un argument")
        return None
    access_path = dic_save[save_key]["emplacement"]#on récupère l'emplacement actuel de joueur dans sa sauvegarde
    access_path_list = access_path.split("/")[1:]
    new_access_path_list = []
    for i in range(len(access_path_list)):  #on reprend la même liste mais en
        #remettant les "/" qui ont été enlevés par le .split()
        new_access_path_list.append("/" + access_path_list[i])
    #on crée une liste des endroits accessibles depuis son répertoire
    #on regarde l'argument et on agit en fonction-------------------
    new_path = ""  #c'est la valeur qui va remplacer "emplacement" dans save_dic
    #on détermine si l'argument qu'il a entré correspond à un lieu disponible
    if possibilities != None :
        verif_arg = search(possibilities, argument)
    else :
        verif_arg = False
    #----------------------------------------------
    if verif_arg :#s'il peut se déplacer, on change new_path vers le nouvel endroit
        new_access_path_list.append(argument)

    elif argument == "./":
        new_access_path_list = new_access_path_list[0:-1]
    else:
        print(f"\"{argument}\" n'est pas un argument reconnu")
    #---------------------------------------------------------------
    for i in new_access_path_list:
        new_path += i
    #print(f"Vous êtes maintenant dans : {new_path}")
    dic_save[save_key]["emplacement"] = new_path  #on enregistre le déplacement directement dans la save
    exporter("save", dic_save)


def Terminal(save_key) -> None:
    print(Fore.RED + Style.BRIGHT + "```Terminal",
          Fore.GREEN + "                     -h pour de l'aide")
    time.sleep(0.5)
    print(Fore.BLUE)
    print("~Loading~")
    time.sleep(0.5)
    while True:
        #entrée de la commande
        print(Fore.WHITE + Style.NORMAL)
        print("{")
        entree = input()
        #séparation de la commande et de l'agument
        decomposition = entree.split(" ")
        cmd = decomposition[0]
        if len(
                decomposition
        ) != 1:  #on vérifie que l'argument existe et si oui on le récupère
            argument = decomposition[1]
        else:
            argument = None  #il faut quand même déclarer la variable mtn sinon ça pose des problèmes pour la commande cd
        del decomposition, entree
        #-----------------------------------------
        print("}\n")
        time.sleep(0.5)
        print(Fore.BLUE + Style.BRIGHT + "~running task~")
        time.sleep(0.3)
        print(Fore.CYAN + Style.NORMAL)

        #ici la liste des commandes--------------------------
        if cmd == "exit":  #sortie du Terminal
            break

        elif cmd == "tkt":  #commande custom/easter egg
            print("->LOL c'est nul")
            time.sleep(0.3)

        elif cmd == "code_cadeau":
            print(
                "##### TA MERE ESPECE DE ###### T'AS VRAIMENT CRU QUE CA MARCHAIT COMME CA ON N'EST PAS ### NON PLUS (cette remarque n'a pas été approuvée par le directeur)\n"
            )
            time.sleep(4)
            print(
                "PUTAIIIIIIIIIIN C'EST VRAIMENT TOUS DES ####### CES JOUEURS\n(de Théobald, le directeur n'a toujours pas approuvé cette remarque)"
            )

        elif cmd == "pow":  #afficher l'emplacement sur la carte en mode chemin d'accès linux
            access_path = dic_save[save_key]["emplacement"]
            print(f"répertoire : {access_path}")
            list_path = access_path.split("/")
            emplacement = list_path[len(list_path) - 1]
            print(f"\nvous êtes ici : /{emplacement}")

        elif cmd == "ls":  #affiche tous les lieux dispo
            ls(save_key, map, True)

        elif cmd == "autres":
            print(
                "Bien essayé petit ####### de cheater. Désolé il est tard j'ai tendance à m'énerver assez vite. (de Théobald, toujours pas approuvé par le directeur)"
            )

        elif cmd == "cd":  #se tp à un autre lieu
            possibilities = ls(save_key, map, False)
            cd(save_key, argument, possibilities)

        elif cmd == "-h":  #affiche toutes les commandes
            for i in dic_cmd.keys():
                time.sleep(0.1)
                print(f" { i } : { dic_cmd[i] } \n")

        else:
            print(f"command \"{cmd}\" undefined ")
        #-------------------------------------------------

    print(Fore.BLUE + Style.BRIGHT + "~fermeture du processus @ctif~\n")
    time.sleep(1)
    print(Fore.RED + "```", Fore.WHITE, Style.NORMAL)

    return None
#---------------------------------------------------------------------------

#random des répliques des pnj------------------------#
def replique_pnj():
    with open("replique.csv", mode='r', newline='') as replique:
        replique_pnj = list(replique)
        print("\n" + random.choice(replique_pnj))


#combat----------------------------------------------#

#.isnumeric()



def gagner(nombref, nom_de_monstre, tour):
    for i in range(4):
        print(f"\nVous avez battu {nombref}/{nombref} {nom_de_monstre} en {tour} tours!")
        print(Fore.BLUE + Style.BRIGHT+"\nFélicitation ! Vous remportez ce combat !")
        time.sleep(1)
        clearConsole()
        print(f"\nVous avez battu {nombref}/{nombref} {nom_de_monstre} en {tour} tours!")
        print(Fore.CYAN + Style.NORMAL+"\nFélicitation ! Vous remportez ce combat !")
        time.sleep(1)
        clearConsole()
    return
#l'ennemi attaque ou defend en fonction de la variable action dans action_ennemi()


#--------------------------------------------------#
def ecran_accueil():
    print(27 * '-+' + "\n{" + 20 * ' ' + "Bienvenue sur" + 19 * " " + "}" +
          "\n{" + 52 * ' ' + "}" + "\n{" + 21 * ' ' + "Code World" + 21 * " " +
          "}\n" + 27 * '+-' + "\n")
    print(19 * ' ' + "1/ \"New Game\"\n" + 19 * ' ' + "2/ \"Continue\"\n" +
          19 * ' ' + "3/ \"Credits\"\n")
    rep = str(input("entrez votre choix : "))
    while rep != "1" and rep != "2" and rep != "3":
        rep = str(input("entrez votre choix : "))
    if rep == "1":
        clearConsole()
        save_key = start("1")
    if rep == "2":
        clearConsole()
        save_key = start("2")
    if rep == "3":
        clearConsole()
        print("\n" + 28 * ' ' + "Crédits :\n" + "\n" + 13 * ' ' +
              "directeur projet/développeur/scénariste :\n" + 28 * ' ' +
              "Paul-Evan\n\n" + 15 * ' ' +
              "sous directeur projet/développeur :\n" + 28 * ' ' +
              "Théobald\n")
        save_key = ecran_accueil()
    return save_key


#choix du pseudo et création de la sauvegarde------#
def choixPseudo(ng) -> str:
    if ng == "1":  #le joueur n'a jamais joué, on crée une save avec son pseudo (scénario normal)
        rep = ' '
        while rep != "oui":
            perso = input("choisissez le nom de votre personnage : \n")
            print(f"\nVoulez-vous être : {perso}?")
            rep = input("\noui/non :\n")
        #création d'une sauvegarde:
        dic_save[perso] = {"personnage": perso}
        exporter("save", dic_save)
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


#choix de la classe---------------------------------#
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


#vérifie possibilité de la classe ------------------#
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


#assure le joueur de son choix -----------------------#
classe = ""


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
    exporter("save",dic_save)


    return None


#-----------------------------------------------------#
#lancement du jeu----------------------------------#
def start(ng):
    clearConsole()
    print("bienvenue dans code World !")
    save_key = choixPseudo(ng)  #IMPORTANT ici on récupère la clé de sauvegarde
    print(
        "Félicitation voyageur du code, apprêtez-vous à entrer dans Code World !"
    )
    clearConsole()
    return save_key
    #début du jeu----------------#


#-------------------------------------------------------#


#--------------------------------------------------#
def inventaire(save_key, classep):
    list_id_item = separateur(",", dic_save[save_key]["inventaire"])
    it = []
    for i in range(len(list_id_item)):
        it.append(dic_item[list_id_item[i]]["nom"])
    if classep == "guerrier":
        print("\n#----------------------------------------\n statistiques actuelles de {0} :\n force : {1}/100 \n defense : {1}/100 \n HP : {2}/100\n#--------------------\n".format(save_key, guerrier["force"], guerrier["defense"], guerrier["HP"]))

    elif classep == "mage":
        print("\n#----------------------------------------\n statistiques actuelles de {3} : \n force : {0}/100 \n defense : {1}/100 \n HP : {2}/100\n#--------------------\n".format(mage["force"], mage["defense"], mage["HP"], save_key))

    print(f"vos objets :")
    rep = ""
    for i in it :
        rep += i + ", "
    print(rep)
    print("\n#----------------------------------------")




#auberge--------------------------------------------#
def auberge_1():
    a = "bien et vous ?"
    dial = input(
        "Aubergiste : Bienvenue à l'auberge CodeX ! Comment allez-vous ?\n\nchoix : {0}\n\n"
        .format(a))
    if dial != a:
        print("\nHaha...d'accord super...")
    else:
        print("\nMerci beaucoup ! ")
    quete1()


def auberge_hub(save_key, classep):
    clearConsole()
    print(20 * ' ' + "Bienvenue à l'auberge CodeX !")

    def aub1():
        rep = str(
            input(
                "Que faire ? \nchoix : \n fouille\n parler a l'aubergiste\n prendre une biere\n parler a un client\n quitter l'auberge\n"
            ))
        if rep != "fouille" and rep != "parler a l'aubergiste" and rep != "prendre une biere" and rep != "parler a un client" and rep != "quitter l'auberge":
            clearConsole()
            auberge_hub()
        elif rep == "fouille":
            inventaire(dic_save[save_key]["classe"], save_key)
            aub1()
        elif rep == "parler a l'aubergiste":
            print(" ")
            aubergiste()
            aub1()
        elif rep == "prendre une biere":
            clearConsole()
            print("*burp*\n")
            input()
            clearConsole()
            aub1()
        elif rep == "parler a un client":
            replique_pnj()
            aub1()
        elif rep == "quitter l'auberge":
            clearConsole()
            auberge_foret(save_key, classep)
        return

    aub1()
    return


def aubergiste():  #quand le joueur lui parle librement
    print("Aubergiste : \"Hey, que voulez vous ?\"")
    rep = input(
        "\nchoix :\n -\"rien\" \n -\"rappelez moi la quete s'il vous plait\" \n"
    )
    if rep != "rien" and rep != "rappelez moi la quete s'il vous plait":
        aubergiste()
    elif rep == "rien":
        replique_pnj()
        return ()
    elif rep == "rappelez moi la quete s'il vous plait":
        print(
            "\n Bien sûr, j'ai un problème avec le fichier \"forêt\" d'à côté. Des virus rôdent et corrompent nos vivres. Aidez moi même si je ne vous en suppli pas.\n"
        )


def foret_hub_tuto(save_key, classep):
    clearConsole()
    mouv = str(
        input(
            "vous voilà dans la forêt, les sons se mélangent mais le bruit de votre clavier reste constamment présent tandis que vous avancez :\n\n avancer\n\n"
        ))
    if mouv != "avancer":
        clearConsole()
        mv = "mouvement : "
        mouv = str(input("vous voilà dans la forêt, les sons se mélangent mais le bruit de votre clavier reste constamment présent tandis que vous avancez :\n avancer\n{0}".format(mv)))
    else:
        print("*CRACK*")
        print("Un bruit attire votre attention alors que vous lisez cette phrase. Lorsque vous vous retournez, vous le voyez : un virus.\nCelui-là semble faible mais féroce, il est de votre devoir de le combattre.")
    act = str(input("choix :\n combattre\n ...\n"))
    if act != "combattre" and act != "...":
        print("Argh, il vous attaque !\n")
        combat(save_key, classep, 1, 2, 1, 0)
    elif act == "combattre":
        print("Quel courage !\n")
        combat(save_key, classep, 1, 2, 1, 0)
    elif act == "...":
        print("...Eh bien...mais.. *REVEILLEZ-VOUS !* ..ah merci...\n")
        combat(save_key, classep, 1, 2, 1, 0)



#lancement quete n°1--------------------------------#
def quete1():
    print(
        "Dites...j'ai un problème avec le fichier d'à côté. Des virus rôdent et corrompent nos vivres."
    )
    quete = input(
        "Seriez-vous d'accord pour m'aider à les combattre ?\n\nchoix : oui/non\n\n"
    )
    if quete != "oui":
        rep = input(
            "\nMais..pourquoi refuser de jouer ?\n\nchoix : bon d'accord / bon d'accord \n\n"
        )
        repm = "bon d'accord"
        if rep != repm:
            print("quoi ?")
            quete1()
        else:
            pass
    else:
        print("Oh ! Merci beaucoup voyageur !")
        clearConsole()


def fichierq1(save_key):
    print(20 * ' ' + "*Vous avez accepté la quête \"fichier corrompu\"*\n")
    print(
        "Vous vous rendez maintenant dans le fichier \"forêt\" sans savoir ce que vous allez y rencontrer...vous devriez fouiller vos poches...\n"
    )
    fouille = str(input("choix : fouille\n\n"))
    f = "fouille"
    while fouille != f:
        print("\n\"je devrais fouiller mes poches\" vous dites vous\n")
        fouille = str(input("choix : fouille\n"))
    inventaire(save_key, dic_save[save_key]["classe"])
    print("Félicitation ! Comme vous pouvez le constater, vous possédez une jauge de force et de defense qui vous serviront dans les combats hostiles qui vous attendent...Votre niveau d'HP sera aussi impacté. Puisse que votre équipement évolue à la vitesse de vos aventures")

def sortie_tuto(save_key: str) ->None:
    print(f"??????? : Vous ne vous en êtes pas trop mal sorti contre ces virus, même si sans moi vous seriez mort mais bon...\n")
    time.sleep(1)
    print("??????? : Je suis aussi aventurier dans cette région mais dites moi... Qui êtes-vous ?\n")
    print(f"vous : - {save_key} ! et vous ?")
    print("??????? : Uwu_Kikoulol_uwU, pour vous servir.")
    print("\nUwu_Kikoulol_uwU : Je vous ferai remarquer qu'il est peu prudent de donner votre réelle identité au premier venu, surtout sans un bon VPN.")
    time.sleep(1)
    print("\nUwu_Kikoulol_uwU : Je vous conseille d'aller vous équiper à Monstadt avant quoi que ce soit d'autre. Les magasins y sont fournis, vous y trouverez le nécessaire.")
    time.sleep(2)
    print("\n(Votre tenue a été déchirée pendant le combat et ne vous procurera que peu de protection pour les combats à venir)")

def auberge_foret(save_key, classep):
    rep = str(input("choix :\n partir foret \n partir auberge\n"))
    if rep != "partir foret" and rep != "partir auberge":
        print("pô compris")
        rep = str(input("choix :\n partir foret \n partir auberge"))
    elif rep == "partir auberge":
        auberge_hub(save_key, classep)
    elif rep == "partir foret":
        foret_hub_tuto(save_key, classep)



def main():
    save_key = ecran_accueil()
    #il faudra reprendre directement là où le joueur s'était arrêté s'il avait déjà une save
    classep = dic_save[save_key]["classe"]
    #auberge_1()
    #fichierq1(save_key)
    #exporter("save", dic_save) #point de sauvegarde
    #auberge_foret(save_key, classep)




#combat('tkt', 'mage', 1, 2, 0)

#Terminal("tkt")
#sortie_tuto("tkt")
main()
