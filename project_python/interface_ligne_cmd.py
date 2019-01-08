import sys
import cmd
import argparse
from math import *
import os
import os.path
import glob
import getopt
import codecs
# permet la conversion de l'ascii en utf-8
import markdown2
# utilise pour la conversion en html
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
                # fait une liste de chaque fichier contenue 
                # dans le chemin contenue dans argv
                for ligne in path_file:
                    # cherche le fichier de type .md est dans cet liste
                    if ".md" in ligne:
                        file = ligne
                        file = os.path.join(argv[3],file)
                        #je relie le chemin avec le nom du fichier
            else :
                print"Le chemin: ",argv[3], "\n n'existe pas ou n'est pas trouve."
            
        if "-o" in argv:
            result = os.path.exists(argv[5])
            # test si un chemin existe 
            if result == True:
                path_file = os.listdir(argv[5])
                # fait une liste de chaque fichier contenue
                # dans le chemin contenue dans argv[5]
                if not os.path.isfile('test.html'):
                    # si ce fichier est trouve dans la liste
                    # alors sera supprime puis reimporte
                    file1 = os.path.join(argv[5],"test.html")
                    # si il est pas alors on associe le nom du fichier 
                    # aux chemin 
                    with codecs.open(file ,"r","utf-8") as file:
                        # ouverture en lecture du fichier a convertir 
                        lignes = file.readlines()
                        # import du contenue du fichier 
                        with codecs.open (file1,"w","utf-8") as file1:
                            # creation et ouverture du fichier qui va
                            # contenir la conversion en html
                            for ligne in lignes:
                                ligne = markdown2.markdown(ligne)
                                # conversion ligne par ligne en html 
                                file1.write(ligne)
                                # chaque ligne convertit sera ecrit
                                # dans le fichier de destination
                                file1.write("\n")                      
                 
            else :
                file1 = os.path.join(argv[5],"test.html")
                os.remove(file1)
                # si le fichier est deja dans dans le dossier de destination
                # alors le fichier sera supprime
            print"Le chemin: ",argv[6], "\n n'existe pas ou n'est pas trouve."
            print"chemin du dossier contenant les fichier du site est: ", argv[5]
        if "-t" in argv:
            print("veuillez remplacer dans le fihier template html le replace_me par votre nom")
            
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
            # signifie que cette option n'est pas obligatoire
        )
        parser.add_argument(
            "-t",
            "--templatedirectory",
            help="chemin absolue des fichiers html du site",
            required=False,
            # signifie que cette option n'est pas obligatoire
        )
        args = parser.parse_args()
        # ces differentes lignes avec argparse permet l'affichage d'erreur et d'aider 
        # l'utilisateur a utilise l'outils
    if len(argv):
        print"erreur , Manque d'argument veuillez faire -h pour voir comment realiser la commande"
        # Si liste vide alors la commande n'a pas d'argument et donc renvoie une erreur         


if __name__ == "__main__":
    main(sys.argv)
