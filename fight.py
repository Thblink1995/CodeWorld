from colorama import *
import time
from misc import *

def fight():
    raise NotImplementedError

def gagner(nombref, nom_de_monstre, tour):
    for i in range(4):
        print(f"\nVous avez battu {nombref}/{nombref} {nom_de_monstre} en {tour} tours!")
        print(Fore.BLUE + Style.BRIGHT+"\nFélicitation ! Vous remportez ce combat !")
        time.sleep(1)
        clear()
        print(f"\nVous avez battu {nombref}/{nombref} {nom_de_monstre} en {tour} tours!")
        print(Fore.CYAN + Style.NORMAL+"\nFélicitation ! Vous remportez ce combat !")
        time.sleep(1)
        clear()
    return