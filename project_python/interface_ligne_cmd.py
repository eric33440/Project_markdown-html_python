import sys
import cmd
import argparse
from math import *
import os
import os.path
import glob
import getopt


def main():
    # extern = input()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_true"
    )
    parser.add_argument(
        "-i",
        "--input-directory",
        help="define a folder for the file in markdown",
    )
    parser.add_argument(
        "-o",
        "--output-directory",
        help="define a folder for the file of static site",
    )
    parser.add_argument(
        "-t",
        "--template-directory",,
    )
    parser.add_argument(
        "-h",
        "--help",
        help="define a folder for the file of static site",
    )
    args = parser.parse_args()
    if args == "-i":
        file = glob.glob(
            "/home/eric/workspace_python/project_python/fichier source/*.md"
        )
        print(
            "les fichiers mardown se trouve : /home/eric/workspace_python/project_python/fichier source/"
        )
        print("Et il y a :{file}")
    if args.verbose:
        print("verbosity turned on")


    # glob.glob permet de trouver un motif et retourne une liste d'element contenant ce motif
    # pour notre cas cela retourne tout les fichiers markdown dans le chemin indique
    # with open(file,"r")file:
    #    file.read(line)
    # with open("", "w") as file:
    # file.write("<!DOCTYPE html>")
    # file.write("<html>")


if __name__ == "__main__":
    main()
