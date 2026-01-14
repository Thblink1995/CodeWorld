import colorama
from colorama import *
import time
import misc as m
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

def ls(save_key: str, map: dict, visible: bool, dic_save:dict) -> list:
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

def cd(save_key: str, argument: str, possibilities: list, dic_save:dict) ->None:
    """
    entrée :
      save_key -> str -> clé de la sauvegarde
      argument -> str -> ce qu'a écrit le joueur derrière "cd"
      possibilities -> list -> liste des emplacements que le joueur peut atteindre depuis sa position
    sortie :
      pas de sortie
      -> met la nouvelle position du joueur directement dans dic_save
    """
    if argument is None :
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
    m.export_file("save", dic_save)

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

def Terminal(save_key, dic_save:dict) -> None:
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