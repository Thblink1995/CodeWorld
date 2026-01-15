# -*- coding: utf-8 -*-
from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from misc import *


def choixClasse(save_key, classes_dico):
    raise NotImplementedError

def new_player():
    pseudo = str(input("Quel est votre identifiant, entité : "))
    if not no_space_string(pseudo):
        print("Un identifiant ne peut pas contenir d'espace")
        return new_player()
    clear()

    raise NotImplementedError

def choix_sauvegarde():
    raise NotImplementedError

def ecran_accueil_temp():
    print(27 * '-+' + "\n{" + 20 * ' ' + "Bienvenue sur" + 19 * " " + "}" +
          "\n{" + 52 * ' ' + "}" + "\n{" + 21 * ' ' + "Code World" + 21 * " " +
          "}\n" + 27 * '+-' + "\n")
    print(19 * ' ' + "1/ \"New Game\"\n" + 19 * ' ' + "2/ \"Continue\"\n" +
          19 * ' ' + "3/ \"Credits\"\n")
    rep = str(input("entrez votre choix : "))
    while rep != "1" and rep != "2" and rep != "3":
        rep = str(input("entrez votre choix : "))
    if rep == "1":
        clear()
        save_key = new_player()
    if rep == "2":
        clear()
        save_key = choix_sauvegarde()

    if rep == "3":
        clear()
        print("\n" + 28 * ' ' + "Crédits :\n" + "\n" + 13 * ' ' +
              "directeur projet/développeur/scénariste :\n" + 28 * ' ' +
              "Paul-Evan\n\n" + 15 * ' ' +
              "sous directeur projet/développeur :\n" + 28 * ' ' +
              "Théobald\n")
        save_key = ecran_accueil()
    return save_key


def ecran_accueiltemp2():
    # On utilise des caractères simples (+, -, |) pour les bordures si l'Unicode crash
    from rich.box import ASCII

    logo = "[bold green]CODE WORLD[/bold green]"
    console = Console()
    # L'argument box=ASCII force Rich à ne pas utiliser de caractères spéciaux
    console.print(Panel(
        Align.center(logo),
        title="SYSTEM_INIT",
        box=ASCII,
        border_style="bright_blue"
    ))

    # Utilise Prompt de Rich pour un menu propre qui ne bugge pas
    rep = Prompt.ask(
        "\n[bold yellow]1/[/] New Game\n[bold yellow]2/[/] Continue\n[bold yellow]3/[/] Credits\n\n[white]Choix[/]",
        choices=["1", "2", "3"]
    )

    if rep == "1":
        clear()
        save_key = new_player()

    elif rep == "2":
        clear()
        save_key = choix_sauvegarde()

    elif rep == "3":
        clear()
        # 3. CRÉDITS STYLISÉS : On remplace les calculs d'espaces par un Panel ou une Table
        table = Table.grid(padding=1)
        table.add_column(justify="right", style="cyan")
        table.add_column(justify="left", style="white")

        table.add_row("Directeur / Scénariste :", "Paul-Evan")
        table.add_row("Sous-directeur / Dev :", "Théobald")

        console.print(Panel(
            table,
            title="[bold red] STAFF_LOGS [/]",
            expand=False,
            border_style="red"
        ))

        # Pause pour laisser lire
        Prompt.ask("\n[dim]Appuyez sur Entrée pour revenir au terminal principal...[/]")
        clear()
        save_key = ecran_accueil()  # Retour récursif au menu

    return save_key


from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich.box import DOUBLE

console = Console()


def ecran_accueil():
    # 1. Le logo original en caractères de bloc (Unicode)
    logo = """
[bold green]
░█▀▀░█▀█░█▀▄░█▀▀░░░█░█░█▀█░█▀▄░█░░░█▀▄
░█░░░█░█░█░█░█▀▀░░░█▄█░█░█░█▀▄░█░░░█░█
░▀▀▀░▀▀▀░▀▀░░▀▀▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀░
[/bold green]
    """

    # 2. Affichage du Header avec bordure double
    console.print(Panel(
        Align.center(logo),
        title="[bold white]v1.0.4-STABLE[/]",
        subtitle="[blink red]CONNECTION...[/]",
        border_style="bright_blue",
        box=DOUBLE
    ))

    console.print("\n")

    # 3. Utilisation du Prompt pour la logique de sélection
    # choices gère le "while" automatiquement
    rep = Prompt.ask(
        "[bold cyan]Système prêt. Choisissez une option[/]",
        choices=["1", "2", "3"],
        default="1"
    )

    if rep == "1":
        clear()
        return new_player()

    elif rep == "2":
        clear()
        return choix_sauvegarde()

    elif rep == "3":
        clear()
        # Affichage des crédits dans un style "Logs système"
        credits_txt = (
            "[bold green]DÉVELOPPEUR PRINCIPAL :[/] Paul-Evan\n"
            "[bold green]CO-DÉVELOPPEUR         :[/] Théobald\n"
            "\n[dim italic]Moteur de rendu : Rich Library v13.0+[/]"
        )
        console.print(Panel(credits_txt, title="CREDITS", border_style="green"))

        Prompt.ask("\n[white]Appuyez sur ENTRÉE pour revenir[/]")
        clear()
        return ecran_accueil()
    return None