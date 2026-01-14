import misc as m
import fight
import inventaire
import time
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


def auberge_hub(save_key, classep, dic_save):
    m.clear()
    print(20 * ' ' + "Bienvenue à l'auberge CodeX !")

    def aub1():
        rep = str(
            input(
                "Que faire ? \nchoix : \n fouille\n parler a l'aubergiste\n prendre une biere\n parler a un client\n quitter l'auberge\n"
            ))
        if rep != "fouille" and rep != "parler a l'aubergiste" and rep != "prendre une biere" and rep != "parler a un client" and rep != "quitter l'auberge":
            m.clear()
            auberge_hub()
        elif rep == "fouille":
            inventaire.print(dic_save[save_key]["classe"], save_key)
            aub1()
        elif rep == "parler a l'aubergiste":
            print(" ")
            aubergiste()
            aub1()
        elif rep == "prendre une biere":
            m.clear()
            print("*burp*\n")
            input()
            m.clear()
            aub1()
        elif rep == "parler a un client":
            m.replique_pnj()
            aub1()
        elif rep == "quitter l'auberge":
            m.clear()
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
        m.replique_pnj()
        return ()
    elif rep == "rappelez moi la quete s'il vous plait":
        print(
            "\n Bien sûr, j'ai un problème avec le fichier \"forêt\" d'à côté. Des virus rôdent et corrompent nos vivres. Aidez moi même si je ne vous en suppli pas.\n"
        )


def foret_hub_tuto(save_key, classep):
    m.clear()
    mouv = str(
        input(
            "vous voilà dans la forêt, les sons se mélangent mais le bruit de votre clavier reste constamment présent tandis que vous avancez :\n\n avancer\n\n"
        ))
    if mouv != "avancer":
        m.clear()
        mv = "mouvement : "
        mouv = str(input("vous voilà dans la forêt, les sons se mélangent mais le bruit de votre clavier reste constamment présent tandis que vous avancez :\n avancer\n{0}".format(mv)))
    else:
        print("*CRACK*")
        print("Un bruit attire votre attention alors que vous lisez cette phrase. Lorsque vous vous retournez, vous le voyez : un virus.\nCelui-là semble faible mais féroce, il est de votre devoir de le combattre.")
    act = str(input("choix :\n combattre\n ...\n"))
    if act != "combattre" and act != "...":
        print("Argh, il vous attaque !\n")
        fight.fight(save_key, classep, 1, 2, 1, 0)
    elif act == "combattre":
        print("Quel courage !\n")
        fight.fight(save_key, classep, 1, 2, 1, 0)
    elif act == "...":
        print("...Eh bien...mais.. *REVEILLEZ-VOUS !* ..ah merci...\n")
        fight.fight(save_key, classep, 1, 2, 1, 0)



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
        m.clear()

def fichierq1(save_key, dic_save):
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

