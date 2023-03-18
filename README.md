# 📂 Duplicate File Remover 🚀
## A CS50 Python project


## Usage 💻

` python duplicate_file_remover.py /path/to/directory `

###### The program will then scan the directory and its subdirectories for duplicate files, and print a list of any duplicate files it finds. It will also ask you whether you want to delete the duplicate files. 💾


## How it works 🤔
###### The program works by first getting a list of all files in the directory and its subdirectories, using the os.walk function.

###### It then groups the files by size, using a dictionary where the keys are file sizes and the values are lists of file paths. Any file groups with more than one path are considered to be duplicates.

######  If you choose to delete the duplicate files, the program then removes all files in each duplicate group except the first one, using the os.remove function. 🔍

# Requirements 📋 
###### The program requires Python 3.5 or later to be installed.
