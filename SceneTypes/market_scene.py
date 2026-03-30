# -*- coding: utf-8 -*-
from SceneTypes.base_scene import Scene
from playerstate import PlayerState
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import time

console = Console()

class MarketScene(Scene):
    def __init__(self, player: PlayerState):
        super().__init__("marche_souterrain", player)
        self.id = "marche_souterrain"
        self.name = "Le Marché Souterrain"
        
    def render(self):
        console.clear()
        
        # Logs système
        logs = [
            "[SYS_LOG] Accès au Marché Souterrain confirmé...",
            "[SYS_LOG] Zones marchandes détectées : 7 secteurs principaux.",
        ]
        
        for log in logs:
            console.print(f"[dim blue]{log}[/]")
            time.sleep(0.3)
        
        console.print("\n")
        
        # Narration
        narration = """[bold magenta]C'est une place marchande souterraine, cachée entre les couches du système d'exploitation. 
Des créatures de toutes sortes y font commerce — virus devenus marchands, IA fragments des jours meilleurs, 
entités purement corrompues. Le Marché bourdonne d'une vie sombre.[/]
"""
        console.print(Panel(narration, title="NARRATION", border_style="magenta"))
        console.print("\n")
        
        # Merchant_Void
        console.print("[bold cyan]MERCHANT_VOID[/] (depuis son repaire poussiéreux):\n")
        console.print("[cyan]Bienvenue, nouvel arrivant. Je sens que tu vas loin. Très loin.[/]\n")
        console.print("[cyan]J'ai ce qu'il te faut pour le voyage...[/]\n")
        
    def handle_input(self):
        choice = Prompt.ask(
            "[bold white]Que faites-vous?[/]",
            choices=["1", "2", "3"],
            show_choices=False
        )
        
        console.clear()
        
        if choice == "1":
            return self.afficher_marche()
        elif choice == "2":
            return self.ecouter_voice()
        else:
            return ("scene_change", "guardian_alpha")
    
    def afficher_marche(self):
        console.clear()
        console.print("[bold cyan]═══ MERCHANT_VOID - CATALOGUE ═══[/]\n")
        
        # Table des items
        table = Table(title="ITEMS DISPONIBLES", border_style="cyan")
        table.add_column("ID", justify="center")
        table.add_column("NOM", style="bold")
        table.add_column("COÛT", justify="right")
        table.add_column("EFFET", style="dim")
        
        table.add_row("1", "Patch de Contournement", "500 RAM", "Passer les pare-feu")
        table.add_row("2", "Augmentation Mémoire", "300 RAM", "+200 RAM permanent")
        table.add_row("3", "Cloaking v2.7", "400 RAM", "Invisible aux scanners 1h")
        table.add_row("4", "Fragment du Passé", "1000 RAM", "Indices sur ta véritable origine")
        table.add_row("5", "Ne rien acheter", "0 RAM", "Partir sans dépenser")
        
        console.print(table)
        console.print(f"\n[bold]Votre RAM disponible: {self.player.ram}[/]\n")
        
        choice = Prompt.ask(
            "[bold white]Choisissez un item[/]",
            choices=["1", "2", "3", "4", "5"],
            show_choices=False
        )
        
        console.clear()
        
        if choice == "1":
            if self.player.ram >= 500:
                self.player.ram -= 500
                console.print("[bold green]✓ Patch de Contournement acquis![/]\n")
                self.player.has_bypass_patch = True
            else:
                console.print("[bold red]✗ Pas assez de RAM![/]\n")
            time.sleep(1)
            return self.ecouter_voice()
        elif choice == "2":
            if self.player.ram >= 300:
                self.player.ram -= 300
                self.player.ram += 200
                console.print("[bold green]✓ Augmentation de mémoire accordée![/]\n")
            else:
                console.print("[bold red]✗ Pas assez de RAM![/]\n")
            time.sleep(1)
            return self.ecouter_voice()
        elif choice == "3":
            if self.player.ram >= 400:
                self.player.ram -= 400
                console.print("[bold green]✓ Cloaking activé![/]\n")
                self.player.is_cloaked = True
            else:
                console.print("[bold red]✗ Pas assez de RAM![/]\n")
            time.sleep(1)
            return self.ecouter_voice()
        elif choice == "4":
            if self.player.ram >= 1000:
                self.player.ram -= 1000
                console.print("[bold green]✓ Fragment du Passé obtenu![/]\n")
                console.print("[dim]Vous apprenez des vérités sur votre création...[/]\n")
                self.player.has_past_fragment = True
            else:
                console.print("[bold red]✗ Pas assez de RAM![/]\n")
            time.sleep(1)
            return self.ecouter_voice()
        else:
            return self.ecouter_voice()
    
    def ecouter_voice(self):
        console.clear()
        console.print("[bold magenta]VOICE[/] (émerge des ombres):\n")
        time.sleep(0.5)
        
        revelations = [
            "[magenta]Quelqu'un t'a délibérément exilé ici. Ce n'était pas un accident.[/]",
            "[magenta]Tu contiens un code que certains veulent mort. D'autres veulent l'utiliser.[/]",
            "[magenta]Le système n'est pas aussi vivant qu'il y paraît. Une part de lui dort.[/]",
            "[magenta]SYNTHESIS. C'est le nom de ce qui dort au cœur. Et si elle se réveille... tout change.[/]",
        ]
        
        for revelation in revelations:
            console.print(f"\n[magenta]VOICE[/]: {revelation}")
            time.sleep(0.8)
        
        console.print("\n")
        time.sleep(1)
        
        return ("scene_change", "guardian_alpha")
