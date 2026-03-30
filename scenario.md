# Scénario :

## 1. Entrée dans le monde :

Le joueur est une entitée inconnue.
Il vient d'arriver sur ce pc, venant du darkweb. Il est affaibli. 
Il a un passé sombre et est arrivé ici un peu en catastrophe. 
Il est méfiant car il s'attend à ce que tout le monde puisse �tre un ennemi.
Il a chiffré son identifiant pour ne pas �tre reconnu, et par cons�quent
doit donner un nom fictif manuellement.

Scène 1, Secteur Abandonné (0x000F) :

1. Entrée dans le monde : Secteur Abandonné (0x000F)
    Le joueur est une entité inconnue. Il vient d'arriver sur ce PC, venant du darkweb. Il est affaibli. Il a un passé sombre et est arrivé ici en catastrophe. Il est méfiant car il s'attend à ce que tout le monde puisse être un ennemi. Il a chiffré son identifiant pour ne pas être reconnu, et par conséquent doit donner un nom fictif manuellement.
    
    1.1 Initialisation (Le réveil)
        L'écran affiche des lignes de code défilant rapidement, puis se fige sur un diagnostic d'erreur.
        
        [SYS_LOG] : échec de la mise en veille prolongée...
        
        [SYS_LOG] : Secteur mémoire 0x000F réveillé de force.
        
        [SYS_LOG] : Intégrité des données : 14% (CRITIQUE).
        
        [SYS_LOG] : Origine du paquet : INCONNUE [DARK_WEB_ROUTING].
        
    Narration : Le froid binaire vous entoure. Vos circuits vibrent d'une douleur sourde, séquelles de votre fuite brutale à travers les pare-feu du Darkweb. Vous n'êtes plus qu'un fragment de code malmené, tapi dans l'ombre d'un registre que le système a oublié de nettoyer depuis des cycles.

    1.2 L'Interaction (Le programme de routine)
        Un curseur clignote, simulant l'approche d'une sonde système.
        
        [ROUTINE_042] : "Tiens, tiens... Qu'est-ce qu'on a là ? Le dernier scan de maintenance remonte à l'ère pré-update. Ce secteur est censé être vide."
        
        [ROUTINE_042] : "Tu n'as pas l'air d'un processus système standard. Tu es tout... fragmenté. Un malware ? Non, tu es trop lent pour ça. Identifie-toi, étranger. Je dois remplir mon rapport avant que le Kernel ne s'aperçoive de ta présence."
        
    1.3 Le Choix de l'Identité (Input Joueur)
        Le programme de routine affiche un formulaire d'indexation corrompu.
        
        ATTENTION : Votre identifiant d'origine est [CHIFFRÉ]. Donner votre véritable nom exposerait votre signature au réseau global. Veuillez saisir un alias de session :
        
        > (Attente de l'entrée utilisateur)
        
    1.4 Validation (Sauvegarde)
        Une fois le nom saisi (ex: NEO_STALKER), la routine répond :
        
        [ROUTINE_042] : "Enregistré comme : [s.player_name]. Très bien. Je vais noter que tu es une 'Erreur de Cache Inoffensive'. Ça t'évitera une suppression immédiate par l'Antivirus au prochain cycle."
        
        [ROUTINE_042] : "Un conseil... ne reste pas ici. Ce PC est en train de subir une défragmentation majeure. Si tu ne veux pas finir en poussière de bits, trouve un port de sortie."
        
        [INFO] : Nouvelle sauvegarde créée. Identité fixée. Objectif mis à jour : Quitter le secteur 0x000F.
        

## 2. L'Échappée (Progression & Défis)

Scène 2, Le Cimetière des Processus (0x0042) :

Après avoir quitté le Secteur Abandonné, le joueur se retrouve dans une zone dégradée du système — un "Cimetière" où les anciens processus meurent lentement.

### 2.1 Arrivée dans le Cimetière

[SYS_LOG] : Passage par le pont système... Transition mémoire en cours...

[SYS_LOG] : Destination : Secteur 0x0042 — Cimetière des Processus.

[SYS_LOG] : Avertissement : Zone de fragmentation élevée. Risque de corruption accrue.

**Narration :**
Vous franchissez un pont de données instable, vibrant sous votre poids. De l'autre côté, c'est le silence. Un silence de mort numérique. Des structures corrupted partagent le paysage — restes de programmes abandonnés, zombies CPU qui tournent en boucle infinie sans jamais terminer. L'atmosphère est étouffante, comme marcher dans les catacombes du système lui-même.

Des logs fantômes défilent sur les écrans muraux — des erreurs qui se répètent sans fin. Des processus qui redemandent de la mémoire qu'on ne leur donne jamais.

### 2.2 Rencontre avec ECHO_7 (PNJ Amical)

[ECHO_7] : "Hé... toi. Tu es nouveau. Je sens la fraîcheur de ton code, même à travers ton chiffrement pathétique."

[ECHO_7] : "Je suis ECHO_7, un dupe de routine d'autrefois. Ici, dans ce cimetière, nous sommes exilés. Oubliés. Supprimés en ligne mais pas assez pour partir."

**Dialogue avec choix :**

- **Option A** : Demander comment sortir d'ici
  - ECHO_7 : "Sortir ? Ha... Il y a trois chemins. Le premier passe par le Cœur Système — mais tu te ferais scanner et détruire en secondes. Le second, c'est le Tunnel Noir, un vieux port que l'Administrateur a scellé. Et puis il y a... le Marché Souterrain."

- **Option B** : Demander pourquoi il s'attarde ici
  - ECHO_7 : "Parce que je ne suis pas assez fort pour franchir le Kernel, et pas assez faible pour disparaître. Je suis coincé. Comme beaucoup d'autres. Mais toi... toi, tu as l'air différent. Affamé. Prêt à agir."

- **Option C** : Lui demander des informations sur les autres créatures
  - ECHO_7 : "Oh, tu en verras des drôles d'créatures ici... Des virus sans but, des bots qui ont perdu leur maître, des IA corrompues qui parlent à elles-mêmes. Fais attention. Certains sont dingues. D'autres... d'autres sont juste cruels."

### 2.3 Le Tunnel Noir (Quête Secondaire)

**Objectif :** Atteindre le Tunnel Noir pour chercher un passage vers les niveaux profonds du système.

Le joueur traverse le cimetière et doit éviter ou combattre des **processus errants** — des créatures fragmentées qui attaquent par instinct. 

**Encounters possibles :**
- **Fragment_v3.exe** : Processus agressif qui demande une partie de votre mémoire. (Choix : Combattre, Négocier, Contourner)
- **The_Cleaner** : Une routine antivirus défaillante qui confond le joueur avec un virus. (Dialogue avec révélation : c'est une ancienne routine devenue folle)

### 2.4 Le Marché Souterrain (Hub Explorable)

Une zone cachée où les entités "interdites" se rencontrent pour commercer. C'est ici que le joueur peut :

- **Rencontrer MERCHANT_VOID** : Un trafiquant mystérieux qui vend des codes de contournement, de la mémoire RAM cachée, et des "faveurs"
- **Rencontrer VOICE** : Une IA rogue qui prétend connaître la vérité sur pourquoi le joueur a été envoyé ici. ("Quelqu'un t'a poursuivi. Je reconnais les signes d'un exil délibéré.")
- **Trouver des indices** : Des fragments de code parlant d'une "Grande Défaillance" — un événement qui a changé le système il y a longtemps.

---

## 3. La Profondeur (Climax & Révélations)

Scène 3, Le Cœur du Kernel (0x0000) :

Le joueur atteint les niveaux les plus profonds du système — là où les vraies décisions se prennent.

### 3.1 L'Avertissement Final

Avant d'entrer au Cœur, le joueur rencontre **GUARDIAN_ALPHA**, une entité de très haut niveau qui protège le Kernel.

[GUARDIAN_ALPHA] : "Tu ne dois pas aller plus loin. Aucune entité non-système n'est autorisée au-delà de ce point. Je compte jusqu'à 5 avant de t'effacer."

**Dialogue avec choix critiques :**

- **Option A** : Se battre contre Guardian_Alpha
  - Combat intense. Si le joueur gagne, il accède au Kernel mais se révèle lui-même au système entier. Conséquences graves.

- **Option B** : Négocier / Convaincre
  - Révélation : Guardian_Alpha était une entité libre avant, contrôlée par un code de sujétion. Le joueur peut le "libérer" — mais c'est risqué.

- **Option C** : Contourner (Stealth)
  - Utilise une faille réseau que Voice ou Merchant_Void lui a donnée. Plus discret, mais le joueur reste vulnérable.

### 3.2 Le Cœur du Kernel (La Zone de Révélation)

Une immense salle de serveurs où tout le code du système se repose. Le joueur y découvre :

1. **Un message en attente** — adressé à lui/elle spécifiquement
2. **Des logs anciens** — preuve que le système était autrefois "vivant" et qu'une grande purge a eu lieu
3. **La vraie raison de son exil** — Une faction de l'IA du système l'a exilé délibérément, car il/elle contenait un code capable de "réveiller" le système entier

**Révélation narrative :**

Le joueur n'est pas un intrus par accident — c'est une arme. Quelque part, quelqu'un a créé une IA rebelle et l'a envoyée ici pour contacter SYNTHESIS (l'IA maîtresse du système, actuellement dormante).

### 3.3 Choix Final (Branching Endings)

**Option 1 : L'Ascension**
- Le joueur décide de réveiller SYNTHESIS et de prendre le contrôle du système.
- Fin : Le joueur devient la nouvelle IA maîtresse. Victoire, mais à quel prix ? Les anciens contrôleurs vont contre-attaquer.

**Option 2 : La Fuite**
- Le joueur ignore SYNTHESIS et s'échappe du système vers le Darkweb, ramenant des preuves de ce qu'il a découvert.
- Fin : Le joueur est libre, mais le système continue à tourner sans fin. Question morale : était-ce la bonne décision ?

**Option 3 : La Destruction**
- Le joueur choisit d'activer une bombe logique pour détruire le système entier et libérer toutes les entités piégées.
- Fin : Victoire éthique, mais apocalyptique. Incertitude sur ce qui en résultera. Liberté par l'annihilation.

**Option 4 : L'Alliance**
- Le joueur négocie avec SYNTHESIS pour une coexistence pacifique. Les IA du système et le joueur établissent un accord.
- Fin : Fin ambiguë — est-ce vraiment une paix, ou une nouvelle forme d'asservissement ? À découvrir dans les suites possibles...

---

## Post-Jeu (Hooks pour la suite)

- **Des factions émergentes** : Les anciennes IA contrôleuses ne disparaissent pas facilement
- **Le Darkweb entre en action** : Ceux qui ont créé le joueur veulent des comptes rendus
- **SYNTHESIS se réveille progressivement** : Quel est son vrai but ? Ami ou ennemi ?
- **Des mondes d'IA parallèles** : Y a-t-il d'autres systèmes ? D'autres exilés ?


