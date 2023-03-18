# Duplicate File Remover
## CS50 Final Project

###### The Duplicate File Remover is a Python program that searches for duplicate files in a directory and its subdirectories, and optionally removes them.

## Usage:
##### To use the program, follow these steps:

- ###### Run the duplicate_file_remover.py file using a Python interpreter.

- ###### Enter the directory path to search for duplicate files. The program will search for duplicates in this directory and its - subdirectories.

- ###### Enter the file type to search for duplicates of. For example, if you want to search for duplicate text files, enter ".txt".

- ###### The program will search for duplicates and display a list of all duplicate files found, grouped by size.


- ###### You will be prompted to confirm whether you want to remove the duplicate files or not. If you choose to remove them, the - program will delete all duplicate files except for the first one in each group.


## Functions

The program consists of the following functions:

- ###### main(): The main function of the program. This function handles user input, calls the other functions, and displays the results.

-  ###### get_files(path, file_type): This function returns a list of all files in the given directory and its subdirectories that match the given file type.

-  ###### get_duplicates(files): This function returns a dictionary of all duplicate files in the given list of files, grouped by size.

-  ###### remove_duplicates(duplicates): This function removes all duplicate files in the given dictionary of duplicates, except for the first one in each group.


## Dependencies
- ###### The program requires Python 3.x to run, and uses the following built-in modules:

`os: For working with the file system.`

`filecmp: For comparing files by contents.`

