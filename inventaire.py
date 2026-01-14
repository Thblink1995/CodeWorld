import misc as m

def print(save_key, classep, dic_save, dic_item):
    """
    imprime l'inventaire actuel dans la console
    """
    list_id_item = m.separateur(",", dic_save[save_key]["inventaire"])
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