# Write a function that recursively scrolls a directory and displays those files whose name matches 
# a regular expression given as a parameter or contains a string that matches the same expression. 
# Files that satisfy both conditions will be prefixed with ">>"

import os
import re

def search_files(path, regex):
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(file):
            search_files(file, regex)
        else:
            if re.match(regex, file):
                print('>>', file)
            elif re.search(regex, file):
                print(file)

def main():
    search_files("./lab6",r'\.py$')

main()