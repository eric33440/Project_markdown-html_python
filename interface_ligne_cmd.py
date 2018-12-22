import sys
import cmd
import argparse
from math import *
import os
import glob

parser = argparse.ArgumentParser()
parser.parse_args()


def main():
    file = glob.glob("/home/eric/workspace_python/project_python/*.md")
    path = "/home/eric/workspace_python/project_python"
    file = file - path
    print(file)
    # with open("", "w") as file:
    # file.write("<!DOCTYPE html>")
    # file.write("<html>")


if __name__ == "__main__":
    main()
