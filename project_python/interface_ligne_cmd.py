import sys
import cmd
import argparse
from math import *
import os
import os.path
import glob
import getopt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_true"
    )
    parser.add_argument("-i", "--input-directory")
    parser.add_argument("-o", "--output-directory")
    args = parser.parse_args()
    if args.verbose:
        print("verbosity turned on")
    file = glob.glob("/home/eric/workspace_python/project_python/*.md")
    parser = argparse.ArgumentParser()
    parser.add_argument("bar", type=argparse.FileType("w"))
    parser.parse_args(["out.md"])
    Namespace(bar=<_io.TextIOWrapper name='out.md' encoding='UTF-8'>)


    # glob.glob permet de trouver un motif et retourne une liste d'element contenant ce motif
    # pour notre cas cela retourne tout les fichiers contenant
    # with open(file,"r")file:
    #    file.read(line)
    # with open("", "w") as file:
    # file.write("<!DOCTYPE html>")
    # file.write("<html>")


if __name__ == "__main__":
    main()
