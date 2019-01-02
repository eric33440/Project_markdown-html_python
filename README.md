# Project_markdown-html_python
Outil convertissant un dossier mardown en HTML


## Outils de conversion mardown vers HTML

Pour faire cela il faut importer le fichier markdown le lire ligne par ligne en remplaçant les équivalent du langage markdown en HTML.
Pour la conversion j'ai utilisé la librairie markdown qui convertit une ligne de mackdown en html. Mais avant sa grâce à la librairie glob j'ai pût trouver le fichier selon le motif du fichier à convertir ici txt puis importation du fichier en mode lecture et d'un autre fichier mode écriture.
Dans le fichier ouvert en lecture on importe dans une variable le contenue à convertir en utilisant le readline qui va nous renvoyer le contenue du fichier par ligne dans une liste.
Dans cette liste on la convertit avec une boucle et on écrit sur le fichier ouvert en écriture la conversion ligne par ligne en HTML.
