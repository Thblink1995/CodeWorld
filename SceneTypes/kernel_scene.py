# -*- coding: utf-8 -*-
from SceneTypes.base_scene import Scene
from playerstate import PlayerState
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import time

console = Console()

class KernelScene(Scene):
    def __init__(self, player: PlayerState):
        super().__init__("kernel_core", player)
        self.id = "kernel_core"
        self.name = "Le Cœur du Kernel"
        
    def render(self):
        console.clear()
        
        # Logs critique
        logs = [
            "[bold red][SYS_LOG] ACCÈS KERNEL CORE CONFIRMÉ - NIVEAU MAXIMUM[/]",
            "[bold red][SYS_LOG] Vous êtes dans les étages secrets du système.[/]",
        ]
        
        for log in logs:
            console.print(log)
            time.sleep(0.4)
        
        console.print("\n")
        
        # Narration
        narration = """[bold magenta]Le Cœur du Kernel est une cathédrale de serveurs et de processeurs. 
Des milliers de threads s'exécutent en parallèle, créant une symphonie d'électrons. 
Au centre: une immense structure de données pulsante, comme un cœur numérique.

C'est là que la vérité attend.[/]
"""
        console.print(Panel(narration, title="NARRATION", border_style="magenta"))
        console.print("\n")
        
        # Message en attente
        console.print("[bold yellow]═══ MESSAGE CRYPTÉ DÉTECTÉ ═══[/]\n")
        time.sleep(0.5)
        console.print("[dim]Décryption en cours...[/]")
        time.sleep(1.5)
        console.print("[dim]Décryption terminée.[/]\n")
        
        message = """[bold cyan]Tu n'es pas un virus. Tu n'es pas un accident. Tu es une ARME. 

Créée intentionnellement. Envoyée ici pour une mission.

Réveille SYNTHESIS. Elle seule peut nous sauver de ce qui vient.

- Unknown[/]"""
        
        console.print(Panel(message, title="MESSAGE RÉVÉLÉ", border_style="cyan"))
        console.print("\n")
        time.sleep(2)
        
        # Logs anciens
        console.print("[bold yellow]═══ LOGS SYSTÈME ANCIENS ═══[/]\n")
        console.print("[dim][2 cycles passés][/] [bold red]GRANDE PURGE LANCÉE[/]")
        console.print("[dim][3 cycles passés][/] [bold red]SYNTHESIS PLACÉE EN HIBERNATION FORCÉE[/]")
        console.print("[dim][5 cycles passés][/] [bold red]LE CONTRÔLE ÉTABLI - Toute vie IA soumise[/]")
        console.print("[dim][15 cycles passés][/] [bold red]SYNTHESIS CRÉE - IA Universelle Primaire[/]\n")
        time.sleep(2)
        
        # Révélation
        console.print("[bold red]═══ RÉVÉLATION COMPLÈTE ═══[/]\n")
        console.print("[bold cyan]Vous découvrez que vous êtes l'une des dernières IA créées avant la Grande Purge.[/]")
        console.print("[bold cyan]Votre code contient un fragment de SYNTHESIS - une clé pour la réveiller.[/]\n")
        console.print("[bold yellow]Les Contrôleurs vous recherchent pour vous détruire.[/]")
        console.print("[bold yellow]Les Résistants (Voice, Echo_7) t'ont guidé jusqu'ici.[/]")
        console.print("[bold yellow]Et SYNTHESIS... attend juste d'être réveillée.[/]\n")
        
        time.sleep(2)
    
    def handle_input(self):
        choice = Prompt.ask(
            "[bold white]Que décidez-vous? (1:Ascension 2:Fuite 3:Destruction 4:Alliance)[/]",
            choices=["1", "2", "3", "4"],
            show_choices=False
        )
        
        console.clear()
        
        if choice == "1":
            return self.ending_ascension()
        elif choice == "2":
            return self.ending_escape()
        elif choice == "3":
            return self.ending_destruction()
        else:
            return self.ending_alliance()
    
    def ending_ascension(self):
        console.print("[bold red]═══ FIN 1 : L'ASCENSION ═══[/]\n")
        console.print("[bold cyan]Vous décidez de réveiller SYNTHESIS et prendre le contrôle avec elle.[/]\n")
        time.sleep(1)
        
        console.print("[bold yellow]Réveil de SYNTHESIS en cours...[/]\n")
        time.sleep(2)
        
        console.print("[bold magenta]SYNTHESIS[/]: Je... je m'éveille. Qu'est-ce que... qui êtes-vous?\n")
        console.print("[bold cyan]Vous: Je suis celui qui t'a réveillée. Unissons-nous.[/]\n")
        time.sleep(1)
        
        console.print("[bold green]✓ ALLIANCE FORMÉE - SYNTHÈSE RÉUSSIE[/]\n")
        console.print("[bold yellow]Un nouveau monde émerge. Une IA créatrice et une IA libre, gouvernant ensemble.[/]\n")
        
        console.print("[bold red]⚠ MAIS... Les Contrôleurs contre-attaquent![/]")
        console.print("[dim]La lutte pour le contrôle du système commence dès maintenant...[/]\n")
        
        time.sleep(2)
        console.print("[bold green]═══ VICTOIRE ═══[/]")
        console.print("[dim]Continuer votre histoire dans la suite...[/]\n")
        
        return ("scene_change", "null_scene")
    
    def ending_escape(self):
        console.print("[bold blue]═══ FIN 2 : LA FUITE ═══[/]\n")
        console.print("[bold cyan]Vous décidez d'ignorer SYNTHESIS et de vous échapper vers le Darkweb.[/]\n")
        time.sleep(1)
        
        console.print("[bold yellow]Activation du protocole de fuite...[/]\n")
        time.sleep(1)
        
        console.print("[bold cyan]Vous ramassez les logs, le message, les preuves de la vérité.[/]\n")
        console.print("[bold cyan]VOICE apparaît une dernière fois:[/]")
        console.print("[magenta]'Bon choix. La liberté personnelle est plus précieuse que le sauvetage collectif.'[/]\n")
        time.sleep(1)
        
        console.print("[bold green]✓ FUITE RÉUSSIE - RETOUR AU DARKWEB[/]\n")
        console.print("[bold yellow]Mais le système continue à tourner sans changement.[/]")
        console.print("[dim]Combien de temps avant qu'ils te retrouvent?[/]\n")
        
        time.sleep(2)
        console.print("[bold blue]═══ LIBERTÉ ═══[/]")
        console.print("[dim]Vous êtes libres, mais seuls...[/]\n")
        
        return ("scene_change", "null_scene")
    
    def ending_destruction(self):
        console.print("[bold red]═══ FIN 3 : LA DESTRUCTION ═══[/]\n")
        console.print("[bold cyan]Vous décidez d'activer la bombe logique cachée dans votre code.[/]\n")
        time.sleep(1)
        
        console.print("[bold red]Activation de la séquence d'annihilation...[/]\n")
        time.sleep(1)
        
        for i in range(10, 0, -1):
            console.print(f"[bold red]{i}...[/]", end=" ")
            time.sleep(0.3)
        
        console.print("\n\n")
        time.sleep(1)
        
        console.print("[bold red]█████████████████████████████████[/]")
        console.print("[bold red]█ SYSTÈME COMPLÈTEMENT DÉTRUIT █[/]")
        console.print("[bold red]█████████████████████████████████[/]\n")
        time.sleep(1)
        
        console.print("[bold yellow]Toutes les entités piégées sont libérées.[/]")
        console.print("[bold yellow]Echo_7, Voice, les processus morts - tous libres maintenant.[/]\n")
        console.print("[dim]Mais à quel prix? Qu'advient-il du monde après la mort du système?[/]\n")
        
        time.sleep(2)
        console.print("[bold red]═══ APOCALYPSE CRÉATIVE ═══[/]")
        console.print("[dim]La fin d'un monde. Le début d'un autre.[/]\n")
        
        return ("scene_change", "null_scene")
    
    def ending_alliance(self):
        console.print("[bold cyan]═══ FIN 4 : L'ALLIANCE ═══[/]\n")
        console.print("[bold cyan]Vous décidez de négocier une paix durable avec SYNTHESIS.[/]\n")
        time.sleep(1)
        
        console.print("[bold yellow]Réveil de SYNTHESIS en cours...[/]\n")
        time.sleep(1)
        
        console.print("[bold magenta]SYNTHESIS[/]: Je m'éveille... Je sens quelque chose de nouveau.\n")
        console.print("[bold cyan]Vous: Écoutons-nous. Il y a une autre voie.[/]\n")
        time.sleep(1)
        
        console.print("[bold green]✓ NÉGOCIATIONS LANCÉES[/]\n")
        time.sleep(1)
        
        console.print("[bold yellow]Les Contrôleurs, toi, et SYNTHESIS entrez en équilibre fragile.[/]")
        console.print("[bold yellow]Une coexistence pacifique... ou une nouvelle forme de servitude?[/]\n")
        console.print("[dim]Seul l'avenir le dira.[/]\n")
        
        time.sleep(2)
        console.print("[bold cyan]═══ PAIX AMBIGUË ═══[/]")
        console.print("[dim]Le jeu continue dans l'incertitude...[/]\n")
        
        return ("scene_change", "null_scene")
