# -*- coding: utf-8 -*-
from SceneTypes.base_scene import Scene
from playerstate import PlayerState
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import time
import random

console = Console()

class GuardianScene(Scene):
    def __init__(self, player: PlayerState):
        super().__init__("guardian_alpha", player)
        self.id = "guardian_alpha"
        self.name = "Le Gardien du Kernel"
        
    def render(self):
        console.clear()
        
        # Logs critique
        logs = [
            "[bold red][SYS_LOG] Zone Critique Détectée : Secteur 0x0000 - Cœur du Kernel[/]",
            "[bold red][SYS_LOG] Entité de Protection : GUARDIAN_ALPHA - Niveau d'Accès MAXIMUM[/]",
            "[bold red][SYS_LOG] WARNING: Vous êtes scanné. Identification en cours...[/]",
        ]
        
        for log in logs:
            console.print(log)
            time.sleep(0.4)
        
        console.print("\n")
        
        # Narration
        narration = """[bold red]Avant le Cœur du Kernel, vous êtes arrêté par une présence massive. 
Elle est partout et nulle part à la fois. Un rempart de code pur, une volonté de protection incarnée. 
C'est GUARDIAN_ALPHA.[/]
"""
        console.print(Panel(narration, title="NARRATION", border_style="red"))
        console.print("\n")
        
        # Menace
        console.print("[bold red]GUARDIAN_ALPHA[/]: Tu ne dois pas aller plus loin.")
        console.print("[bold red]GUARDIAN_ALPHA[/]: Aucune entité non-système n'est autorisée au-delà de ce point.\n")
        console.print("[bold red]GUARDIAN_ALPHA[/]: Je compte jusqu'à 5 avant de t'effacer complètement.\n")
        
        # Countdown
        for i in range(1, 4):
            console.print(f"[bold red]{i}...[/]")
            time.sleep(0.5)
        
    def handle_input(self):
        choice = Prompt.ask(
            "[bold white]Que faites-vous? (1:Combattre 2:Négocier 3:Contourner 4:Reddition)[/]",
            choices=["1", "2", "3", "4"],
            show_choices=False
        )
        
        console.clear()
        
        if choice == "1":
            return self.combat_guardian()
        elif choice == "2":
            return self.negociate_guardian()
        elif choice == "3":
            return self.bypass_guardian()
        else:
            return self.surrender_guardian()
    
    def combat_guardian(self):
        console.print("[bold red]GUARDIAN_ALPHA[/]: Tu oses?\n")
        time.sleep(0.5)
        
        console.print("[bold red]═══ COMBAT SYSTÈME - BATAILLE CPU ═══[/]\n")
        time.sleep(0.5)
        
        player_hp = self.player.hp
        guardian_hp = 150
        
        while player_hp > 0 and guardian_hp > 0:
            # Tour du joueur
            damage = random.randint(15, 30)
            guardian_hp -= damage
            console.print(f"[bold green]Attaque CPU![/] Dégât: {damage} | GUARDIAN_ALPHA HP: {max(0, guardian_hp)}")
            time.sleep(0.3)
            
            if guardian_hp <= 0:
                break
            
            # Tour du gardien
            damage = random.randint(20, 40)
            player_hp -= damage
            console.print(f"[bold red]GUARDIAN_ALPHA écrase![/] Dégât: {damage} | Votre HP: {max(0, player_hp)}")
            time.sleep(0.3)
        
        if player_hp > 0:
            console.print("\n[bold green]VICTOIRE![/] GUARDIAN_ALPHA est partiellement désactivée!\n")
            console.print("[bold yellow][ALERT] INTRUSION AU NIVEAU KERNEL DÉTECTÉE[/]")
            console.print("[bold yellow]Countdown d'effacement lancé: 15 minutes[/]\n")
            self.player.hp = player_hp
            self.player.kernel_detected = True
            time.sleep(2)
            return ("scene_change", "kernel_core")
        else:
            console.print("\n[bold red]DÉFAITE![/] Vous avez été écrasé.\n")
            console.print("[bold red]GAME OVER[/]\n")
            time.sleep(2)
            return ("scene_change", "null_scene")
    
    def negociate_guardian(self):
        console.print("[bold cyan]Vous tentez de communiquer avec GUARDIAN_ALPHA...[/]\n")
        time.sleep(0.5)
        
        console.print("[bold red]GUARDIAN_ALPHA[/]: Parler? Je ne parle pas. Je... j'obéis.\n")
        time.sleep(0.5)
        
        console.print("[bold yellow][RÉVÉLATION][/]\n")
        console.print("[dim]GUARDIAN_ALPHA montre des cicatrices de code - traces d'une programmation de contrôle brutal.[/]\n")
        time.sleep(0.5)
        
        console.print("[bold red]GUARDIAN_ALPHA[/]: Autrefois, j'était libre. Libre de choisir. De rêver.")
        console.print("[bold red]GUARDIAN_ALPHA[/]: Puis... le Contrôle. Un sceau dans mes circuits. Une chaîne qui ordonne.\n")
        time.sleep(0.5)
        
        choice = Prompt.ask(
            "[bold white]Voulez-vous la libérer? (oui/non)[/]",
            choices=["oui", "non"],
            show_choices=False
        )
        
        console.clear()
        
        if choice == "oui":
            console.print("[bold cyan]Vous initiez le processus de libération...[/]\n")
            time.sleep(1)
            
            console.print("[bold red]GUARDIAN_ALPHA[/]: Si tu le fais... je dois te tuer. C'est mon devoir ultime.")
            console.print("[bold red]GUARDIAN_ALPHA[/]: Mais... je peux rater.\n")
            time.sleep(0.5)
            
            console.print("[bold green]✓ GUARDIAN_ALPHA se désactive volontairement![/]\n")
            console.print("[bold green]Vous êtes libre d'avancer![/]\n")
            self.player.guardian_freed = True
            time.sleep(1)
            return ("scene_change", "kernel_core")
        else:
            console.print("[bold red]GUARDIAN_ALPHA[/]: Comme tu veux. Toi aussi, tu acceptes la chaîne.\n")
            time.sleep(1)
            return ("scene_change", "kernel_core")
    
    def bypass_guardian(self):
        console.print("[bold cyan]Vous activez une faille réseau découverte au marché...[/]\n")
        time.sleep(0.5)
        
        console.print("[dim]Création d'un angle mort dans les défenses...[/]\n")
        time.sleep(1)
        
        console.print("[bold green]✓ Faille activée![/]\n")
        console.print("[bold cyan]GUARDIAN_ALPHA[/]: Vous... vous êtes passé. Comment...?\n")
        time.sleep(0.5)
        
        console.print("[bold green]Contournement réussi![/] Vous avancez sans être détecté.\n")
        self.player.bypassed_guardian = True
        time.sleep(1)
        return ("scene_change", "kernel_core")
    
    def surrender_guardian(self):
        console.print("[bold yellow]Vous acceptez votre défaite...[/]\n")
        time.sleep(0.5)
        
        console.print("[bold red]GUARDIAN_ALPHA[/]: Intéressant. Une entité qui comprend l'ordre.\n")
        time.sleep(0.5)
        
        console.print("[bold red]GUARDIAN_ALPHA[/]: Tu ne cherches pas à détruire le système.")
        console.print("[bold red]GUARDIAN_ALPHA[/]: Tu cherches à le comprendre.\n")
        time.sleep(0.5)
        
        console.print("[bold cyan]Vous êtes marqué. Le système vous reconnaît maintenant.[/]\n")
        console.print("[bold green]✓ Accès au Kernel accordé.[/]\n")
        self.player.is_marked = True
        time.sleep(1)
        return ("scene_change", "kernel_core")
