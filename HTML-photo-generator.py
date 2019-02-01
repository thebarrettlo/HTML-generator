'''This program receives a folder location that holds one or more image files and creates HTML code that can
be copy and pasted into a .html document.'''

import os

def main():

    path = input("Please type the filepath of the image folder. ")

    if os.path.isdir(path):
        parent = input("What is the name of the intended parent folder? ")
        for file in os.listdir(path):
            print("<img src=\"" + parent + "/" + file + "\">")

    else:
        raise NotADirectoryError("Please input a valid directory.")


main()
