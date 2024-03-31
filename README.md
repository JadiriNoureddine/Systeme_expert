# Système Expert d'Aide au Diagnostic de Pannes d'Ordinateur

Ce projet est un système expert conçu pour aider à diagnostiquer les pannes d'un ordinateur en se basant sur les symptômes observés par l'utilisateur. Le système utilise une approche de questionnement pour affiner le diagnostic et identifier l'organe défectueux.

## Fonctionnalités

- **Insérer les symptômes observés :** L'utilisateur peut entrer les symptômes qu'il observe sur l'ordinateur.
- **Questionnaire interactif :** Le système pose des questions à l'utilisateur pour recueillir davantage d'informations sur les symptômes.
- **Diagnostic précis :** En se basant sur les symptômes et les réponses du questionnaire, le système identifie l'organe en panne.
- **Affichage des résultats :** Le système affiche l'organe en panne ainsi que d'autres organes potentiellement concernés par les symptômes.
- **Ajouter, Modifier, Supprimer les règles :** En mode Expert le système peut ajouter modifier et supprimer une règle selon le besoin de                                                 l'expert. 

## Utilisation
 
1. Exécutez le programme en utilisant la commande `python main.py`.
2. Suivez les instructions pour insérer les symptômes observés et répondre au questionnaire.
   Par exemple "Ecran noir"
3. En choisissant le mode expert les règles ajoutées seront trouvées dans `rules.json`

## Codes Utilisés

- **systeme_expert.py:** Ce code implémente un système expert de diagnostic de pannes basé sur des règles définies par des symptômes. Les méthodes permettent d'ajouter, de supprimer et de modifier des règles, ainsi que de diagnostiquer des pannes en fonction des symptômes fournis. Les règles sont stockées dans un fichier JSON pour une persistance des données entre les exécutions du programme.

- **main.py:** Ce code crée une application GUI en utilisant Tkinter pour interagir avec le système expert précédemment défini. L'application permet à l'utilisateur de choisir entre le mode Expert et Utilisateur pour gérer les règles ou diagnostiquer des pannes en fonction des symptômes fournis. Les fonctionnalités incluent l'ajout, la modification et la suppression de règles, ainsi que le diagnostic de pannes via des boîtes de dialogue simples.

- **rules.json:** La base de connaissance où les règles sont stockées.
