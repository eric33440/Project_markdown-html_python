import sys
import cmd
import argparse
from math import *
import os
import os.path
import glob
import getopt


def main(argv):
    print("chemin du dossier markdown est: ", argv[3])
    file = glob.glob("/*.md")
    print(file)
    print("chemin du dossier contenant les fichier du site est: ", argv[5])
    parser = argparse.ArgumentParser(description="creation de site statique")
    parser.add_argument(
        "-i",
        "--inputd",
        default="chemin",
        action="append",
        help="chemin absolue des fichiers makedown",
    )
    parser.add_argument(
        "-o",
        "--outputd",
        help="chemin absolue des fichiers html du site",
        required=False,
    )
    parser.add_argument("-t", "--templated", required=False)
    args = parser.parse_args()
    print(argv.inputd)


if __name__ == "__main__":
    main(sys.argv)
