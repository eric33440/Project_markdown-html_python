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
            #file = os.path.join(argv[3],"*.md")
            result = os.path.exists(argv[3])
            if result == True:
                path_file = os.listdir(argv[3])
                #fait une liste de chaque fichier contenue 
                # dans le chemin contenue dans argv
                for ligne in path_file:
                    # cherche le fichier de type .md est dans cet liste
                    if ".md" in ligne:
                        file = ligne
                        file = os.path.join(argv[3],file)
                        #je relie le chemin avec le nom du fichier
                        with open(file ,"r") as file:
                            lignes = file.readlines()
                        print(lignes)
            else :
                print"Le chemin: ",argv[3], "\n n'existe pas ou n'est pas trouve."
            
        if "-o" in argv:
            result = os.path.exists(argv[5])
            # test si un chemin existe 
            if result == True:
                path_file = os.listdir(argv[5])
                if not os.path.isfile('test.txt'):
                    file1 = os.path.join(argv[5],"test.txt")
                    with open(file ,"r") as file:
                        lignes = file.readlines()
                        with open (file1,"w") as file1:
                            for ligne in lignes:
                                file1.write(ligne)
                                file1.write("\n")                      
                        
            else :
                print"Le chemin: ",argv[5], "\n n'existe pas ou n'est pas trouve."
            print"chemin du dossier contenant les fichier du site est: ", argv[4]
            file = glob.glob(argv[5])
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
