import sys
import cmd
import argparse
from math import *
import os
import os.path
import glob
import getopt
import markdown


def main():
    file = glob.glob(
        "/home/eric/workspace_python/project_python/fichier_source/*.txt"
    )
    file1 = glob.glob(
        "/home/eric/workspace_python/project_python/fichier_site_statique/*.txt"
    )
    path = file[0]

    file_html = file1[0]
    # glob.glob permet de trouver un motif et retourne une liste d'element contenant ce motif
    # pour notre cas cela retourne tout les fichiers markdown dans le chemin indique
    # with open(file,"r")file:
    # with open("file1", "w") as file:

    with open(path, "r") as fichiermarkdown:
        # Lecture du fichier qui contient le code markdown
        lignes = fichiermarkdown.readlines()
        # Va permettre de faire que chaque element de la liste sera une ligne
        # Au lieu qu'un seul caractere
        with open(file_html, "w") as file1:  #
            # Ecriture dans le fichier qui va contenir la conversion en html
            for ligne in lignes:
                ligne = markdown.markdown(ligne)
                # Conversion en html de la ligne pointé
                file1.write(ligne)
                file1.write("\n")
                # Ecriture dans le fichier de la conversion effectue
                # En y ajoutant un retour a la ligne pour ne pas mettre les
                # conversion à la suite des autres.


if __name__ == "__main__":
    main()
