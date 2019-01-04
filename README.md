# Project_markdown-html_python
Outil convertissant un dossier mardown en HTML


## Outils de conversion mardown vers HTML

Pour faire cela il faut importer markdown le lire ligne par ligne en remplaçant les équivalent du langage markdown en HTML.
Pour la conversion j'ai utilisé la librairie markdown qui convertit une ligne de mackdown en html. Mais avant sa grâce à la librairie glob j'ai pût trouver le fichier selon le motif du fichier à convertir ici txt puis importation du fichier en mode lecture et d'un autre fichier mode écriture.
Dans le fichier ouvert en lecture on importe dans une variable le contenue à convertir en utilisant le readline qui va nous renvoyer le contenue du fichier ligne par ligne dans une liste.
Dans cette liste on la convertit avec une boucle pour faire la conversion de chaque élement du tableau et on écrit sur le fichier ouvert en écriture la conversion ligne par ligne en HTML.

## interface ligne de commande

Pour ce code il faut importer deux librairie argparse et sys.
Pour avoir des option sur un script python argparse est utilisé
Avant d'ajouter chaque argument on test si on a bien des arguments, ceux qui va contenir les arguments c'est sys.argv
ou plus précisement la liste argv mis en parametre dans la fonction.


