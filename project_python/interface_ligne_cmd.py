import sys
import cmd
import argparse
from math import *
import os
import os.path
import glob
import getopt


def main(argv):
    if len(argv) > 0:
    # Si la liste contenant les arguments 
    # n'est pas vide alors le code suivant 
    # peut s'executer
        if "-i" in argv:
            file = glob.glob("argv[2]")
            print(file)
        if "-o" in argv:
          print"chemin du dossier contenant les fichier du site est: ", argv[4]
          file = glob.glob(argv[4])
        parser = argparse.ArgumentParser(description="creation de site statique")
        parser.add_argument(
            "-i",
            "--inputdirectory",
            default="chemin",
            action="append",
            help="chemin absolue des fichiers makedown",
        )
        parser.add_argument(
            "-o",
            "--outputdirectory",
            help="chemin absolue des fichiers html du site",
            required=False,
        )
        parser.add_argument(
            "-t",
            "--templatedirectory",
            help="chemin absolue des fichiers html du site",
            required=False,
        )
        args = parser.parse_args()

    if len(argv):
        print"erreur , Manque d'argument veuillez faire -h pour voir comment realiser la commande"
    # Si liste vide alors la commande n'a pas d'argument et donc renvoie une erreur         


if __name__ == "__main__":
    main(sys.argv)
