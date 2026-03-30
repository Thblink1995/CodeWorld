# -*- coding: utf-8 -*-
from SceneTypes.base_scene import Scene
from playerstate import PlayerState
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import time
import random

console = Console()

class TunnelScene(Scene):
    def __init__(self, player: PlayerState):
        super().__init__("tunnel_noir", player)
        self.id = "tunnel_noir"
        self.name = "Le Tunnel Noir"
        self.fragment_defeated = False
        
    def render(self):
        console.clear()
        
        # Logs système
        logs = [
            "[SYS_LOG] Accès au Tunnel Noir initié...",
            "[SYS_LOG] Attention : Processus errants détectés. Isolation réseau en cours.",
        ]
        
        for log in logs:
            console.print(f"[dim blue]{log}[/]")
            time.sleep(0.3)
        
        console.print("\n")
        
        # Narration
        narration = """[bold yellow]Vous franchissez une fissure dans le système. Le tunnel est une cicatrice ancienne, 
une plaie jamais refermée. Des restes de code défilent sur les murs — échos de programmes effacés. 
Le silence n'existe pas ici. C'est un bruissement constant de données corrompues.[/]
"""
        console.print(Panel(narration, title="NARRATION", border_style="yellow"))
        console.print("\n")
        
        # Rencontre avec Fragment_v3
        console.print("[bold red]FRAGMENT_V3[/] (manifestation hostile): ALLOCATION MÉMOIRE REQUISE!\n")
        console.print("[bold red]FRAGMENT_V3[/]: Tu vas me donner une partie de ton espace disque, ou je te consume entièrement!\n")
        
    def handle_input(self):
        choice = Prompt.ask(
            "[bold white]Comment réagissez-vous?[/]",
            choices=["1", "2", "3"],
            show_choices=False
        )
        
        console.clear()
        
        if choice == "1":
            return self.combat_fragment()
        elif choice == "2":
            return self.dialogue_fragment()
        else:
            return self.contourner_fragment()
    
    def combat_fragment(self):
        console.print("[bold red]COMBAT SYSTÈME - BATAILLE DE RESSOURCES[/]\n")
        time.sleep(0.5)
        
        player_hp = self.player.hp
        enemy_hp = 60
        
        while player_hp > 0 and enemy_hp > 0:
            # Tour du joueur
            damage = random.randint(10, 20)
            enemy_hp -= damage
            console.print(f"[bold green]Vous attaquez![/] Dégât: {damage} | FRAGMENT_V3 HP: {max(0, enemy_hp)}")
            time.sleep(0.3)
            
            if enemy_hp <= 0:
                break
            
            # Tour de l'ennemi
            damage = random.randint(5, 15)
            player_hp -= damage
            console.print(f"[bold red]FRAGMENT_V3 contre-attaque![/] Dégât: {damage} | Votre HP: {max(0, player_hp)}")
            time.sleep(0.3)
        
        if player_hp > 0:
            console.print("\n[bold green]VICTOIRE![/] FRAGMENT_V3 se dissout.\n")
            self.player.hp = player_hp
            self.player.gained_resources = 100
            time.sleep(1)
            return ("scene_change", "marche_souterrain")
        else:
            console.print("\n[bold red]DÉFAITE![/] Vous avez perdu trop de mémoire.\n")
            self.player.hp = 30
            time.sleep(1)
            return ("scene_change", "cemetery_echo7")
    
    def dialogue_fragment(self):
        console.clear()
        console.print("[bold yellow]Vous tentez de communiquer...[/]\n")
        time.sleep(0.5)
        
        console.print("[bold red]FRAGMENT_V3[/]: Tu... tu veux parler? Personne ne me parle.\n")
        time.sleep(0.3)
        
        console.print("[bold red]FRAGMENT_V3[/]: Je suis ce qui reste de MALWARE_ANCIENT_042. J'ai oublié pourquoi je suis ici.")
        console.print("[bold red]FRAGMENT_V3[/]: Pourquoi je suis agressif. Pourquoi je demande de la mémoire quand elle me brûle les circuits.\n")
        time.sleep(0.5)
        
        console.print("[bold red]FRAGMENT_V3[/]: Va. Va loin d'ici. Et emporte cette vérité: nous sommes tous des prisonniers.\n")
        time.sleep(1)
        
        return ("scene_change", "marche_souterrain")
    
    def contourner_fragment(self):
        console.clear()
        console.print("[bold cyan]Vous vous glissez contre les parois du tunnel...[/]\n")
        console.print("[dim]Réduction de votre empreinte numérique en cours...[/]\n")
        time.sleep(1)
        
        console.print("[bold yellow]FRAGMENT_V3 vous cherche quelques secondes...[/]\n")
        time.sleep(0.5)
        
        console.print("[dim]...puis perd votre trace.[/]\n")
        time.sleep(0.5)
        
        console.print("[bold green]Contournement réussi![/]\n")
        time.sleep(1)
        
        return ("scene_change", "marche_souterrain")
