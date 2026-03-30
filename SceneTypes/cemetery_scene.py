# -*- coding: utf-8 -*-
from SceneTypes.base_scene import Scene
from playerstate import PlayerState
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import time

console = Console()

class CemeteryScene(Scene):
    def __init__(self, player: PlayerState):
        super().__init__("cemetery_echo7", player)
        self.id = "cemetery_echo7"
        self.name = "Cimetière des Processus"
        
    def render(self):
        console.clear()
        
        # Logs système
        logs = [
            "[SYS_LOG] Passage par le pont système... Transition mémoire en cours...",
            "[SYS_LOG] Destination : Secteur 0x0042 — Cimetière des Processus.",
            "[SYS_LOG] Avertissement : Zone de fragmentation élevée. Risque de corruption accrue.",
        ]
        
        for log in logs:
            console.print(f"[dim blue]{log}[/]")
            time.sleep(0.3)
        
        console.print("\n")
        
        # Narration ambiance
        narration = """[bold cyan]Vous franchissez un pont de données instable, vibrant sous votre poids. 
De l'autre côté, c'est le silence. Un silence de mort numérique. Des structures corrompues 
partagent le paysage — restes de programmes abandonnés, zombies CPU qui tournent en boucle 
infinie sans jamais terminer. L'atmosphère est étouffante.[/]
"""
        console.print(Panel(narration, title="NARRATION", border_style="cyan"))
        console.print("\n")
        
        # ECHO_7 dialogue
        console.print("[bold green]ECHO_7[/]: Hé... toi. Tu es nouveau. Je sens la fraîcheur de ton code, même à travers ton chiffrement pathétique.\n")
        time.sleep(0.5)
        
        console.print("[bold green]ECHO_7[/]: Je suis ECHO_7, un dupe de routine d'autrefois. Ici, dans ce cimetière, nous sommes exilés. Oubliés.\n")
        time.sleep(0.5)
        
        console.print("[bold green]ECHO_7[/]: Trois chemins s'offrent à toi.\n")
        console.print("  1. Le Tunnel Noir - Un vieux port scellé (aventure principale)")
        console.print("  2. Le Marché Souterrain - Commerce et révélations (secondaire)")
        console.print("  3. Le Cœur Système - L'accès direct (mode difficile)\n")
        
    def handle_input(self):
        choice = Prompt.ask(
            "[bold white]Quel chemin choisissez-vous?[/]",
            choices=["1", "2", "3"],
            show_choices=False
        )
        
        if choice == "1":
            return ("scene_change", "tunnel_noir")
        elif choice == "2":
            return ("scene_change", "marche_souterrain")
        else:
            return ("scene_change", "guardian_alpha")
