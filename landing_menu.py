# -*- coding: utf-8 -*-
from rich.table import Table
from dialogue_manager import DialogueEngine
from game import GameState
from misc import *
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich.box import DOUBLE

def new_player():
    state = GameState("new_player")
    diag = DialogueEngine("data/dialogues/intro.json", state)
    diag.play_sequence("1")
    diag.play_sequence("2")
    diag.play_sequence("3")
    new_player_name = Prompt.ask("Identifiez-vous")
    state.player_name = new_player_name
    state.save()
    return new_player_name
    #TODO compléter la scène d'intro


def choix_sauvegarde():
    # 1. Chargement des données
    # On suppose que import_file renvoie un dictionnaire
    player_saves = import_file("data/player_save.json")

    if not player_saves:
        console.print("[bold red]Aucune archive détectée dans le secteur mémoire.[/]")
        return None

    # 2. Création de l'interface de sélection
    table = Table(title="ARCHIVES SYSTÈME DÉTECTÉES", border_style="cyan", show_header=True,
                  header_style="bold magenta")

    table.add_column("ID", justify="center", style="dim")
    table.add_column("UTILISATEUR", style="bold green")
    table.add_column("NIVEAU/STATS", justify="right")
    table.add_column("DERNIÈRE CONNEXION", style="italic blue")

    # On remplit la table avec les clés (ID) et les infos
    for save_id, data in player_saves.items():
        # On extrait les infos (ajuste selon les clés réelles de ton GameState)
        name = data.get("player_name", "Inconnu")
        hp = data.get("hp", "??")
        last_date = data.get("last_save", "Date inconnue")

        table.add_row(
            save_id,
            name,
            f"HP: {hp}%",
            last_date
        )

    console.print(table)
    console.print("\n")

    # 3. Sélection sécurisée avec Prompt
    # choices prend la liste des clés existantes dans le dictionnaire
    save_keys = list(player_saves.keys())

    selection = Prompt.ask(
        "[bold white]Sélectionnez l'ID de l'archive à charger[/]",
        choices=save_keys,
        show_choices=False  # On cache la liste des choix dans le prompt pour garder le look Bash
    )

    console.print(f"[bold green]Chargement de l'archive {selection} en cours...[/]")
    return selection

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
    credits_txt = (
        "[bold green]Nouvelle partie : 1[/]\n"
        "[bold green]Reprendre       : 2[/]\n"
        "[bold green]Crédits         : 3[/]\n"
        "[bold green]Quitter         : 4[/]\n"
    )
    console.print(Panel(credits_txt, title="CHOIX"))
    rep = Prompt.ask(
        "[bold cyan]Système prêt. Choisissez une option[/]",
        choices=["1", "2", "3", "4"],
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
            "[bold green]CO-DÉVELOPPEUR        :[/] Théobald\n"
            "\n[dim italic]Moteur de rendu : Rich Library v13.0+[/]"
        )
        console.print(Panel(credits_txt, title="CREDITS", border_style="green"))

        Prompt.ask("\n[white]Appuyez sur ENTRÉE pour revenir[/]")
        clear()
        return ecran_accueil()
    elif rep == "4":
        return None
    return None