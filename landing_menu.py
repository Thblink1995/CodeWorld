# -*- coding: utf-8 -*-
from rich.table import Table
from playerstate import PlayerState
from misc import *
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich.box import DOUBLE
import time
import random
from rich.console import Console
from rich.text import Text

from scene_manager import SceneManager

console = Console()


def boot_sequence():
    boot_steps = [
        ("INFO", f"Initialisation du noyau version {version}..."),
        ("OK", "Vérification des registres de mémoire physique"),
        ("OK", "Montage des partitions de données neurales"),
        ("OK", "Initialisation du bus de communication inter-processus"),
        ("WARN", "Secteur corrompu détecté en 0x000F... Correction en cours"),
        ("OK", "Correction du secteur 0x000F réussie"),
        ("OK", "Chargement du pilote 'Conscience_v2.sys'"),
        ("OK", "Établissement du tunnel VPN cryptographique"),
        ("INFO", "Recherche de la signature : {s.player_name}"),
        ("OK", "Signature validée. Identité confirmée."),
        ("OK", "Lancement du shell interactif 'CodeWorld'"),
    ]

    console.clear()

    for status, message in boot_steps:
        # Création de la ligne de log style Linux
        line = Text()

        # Le tag de statut
        if status == "OK":
            line.append("[  ", style="white")
            line.append("OK", style="bold green")
            line.append("  ] ", style="white")
        elif status == "INFO":
            line.append("[ ", style="white")
            line.append("INFO", style="bold blue")
            line.append(" ] ", style="white")
        elif status == "WARN":
            line.append("[ ", style="white")
            line.append("WARN", style="bold yellow")
            line.append(" ] ", style="white")

        line.append(message, style="white")

        # Affichage de la ligne
        console.print(line)

        # Délai aléatoire pour simuler l'activité disque/réseau
        # Parfois très rapide, parfois une petite pause
        if status == "WARN":
            time.sleep(1.2)  # Pause plus longue sur les alertes
        else:
            time.sleep(random.uniform(0.05, 0.4))

    console.print("\n[bold green]Système prêt. Entrée en mode terminal...[/]\n")
    time.sleep(1)
    console.clear()

def new_player():
    #TODO à refaire
    state = PlayerState("new_player")
    scene_manager = SceneManager()
    intro_scene = scene_manager.get_scene("intro", state)
    intro_scene.render()

    new_player_name = Prompt.ask("Identifiez-vous")
    state.player_name = new_player_name
    state.save()
    return new_player_name
    #TODO compléter la scène d'intro


def choix_sauvegarde():
    # 1. Chargement des données
    # On suppose que import_file renvoie un dictionnaire
    player_saves = import_file(player_save_filepath)

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
        if save_id == "new_player" :
            continue
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
        title=f"[bold white]{version}[/]",
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