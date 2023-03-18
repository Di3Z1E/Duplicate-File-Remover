import os
import filecmp


def main():
    """
    The main function of the program.
    """
    path = input("Enter directory path: ")
    while not os.path.isdir(path):
        path = input("Invalid directory path. Enter a valid path: ")
    file_type = input("Enter file type (e.g. .txt): ")
    files = get_files(path, file_type)
    duplicates = get_duplicates(files)
    if not duplicates:
        print("No duplicate files found.")
    else:
        print("Duplicate files found:")
        for size, paths in duplicates.items():
            print(f"{size} bytes:")
            for path in paths:
                print(f"- {path}")
        choice = input("Do you want to remove the duplicate files? (y/n) ")
        while choice.lower() not in ["y", "n"]:
            choice = input(
                "Invalid choice. Do you want to remove the duplicate files? (y/n) "
            )
        if choice.lower() == "y":
            remove_duplicates(duplicates)
            print("Duplicate files removed.")
        else:
            print("Duplicate files not removed.")


def get_files(path, file_type):
    """
    Returns a list of all files in the given directory and its subdirectories that match the given file type.
    """
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(file_type):
                files.append(os.path.join(dirpath, filename))
    return files


def get_duplicates(files):
    """
    Returns a dictionary of all duplicate files in the given list of files, grouped by size.
    """
    duplicates = {}
    total_files = len(files)
    for i, file in enumerate(files):
        size = os.path.getsize(file)
        if size in duplicates:
            for existing_file in duplicates[size]:
                if filecmp.cmp(file, existing_file):
                    duplicates[size].append(file)
                    break
            else:
                duplicates[size].append(file)
        else:
            duplicates[size] = [file]
        print(f"Processed {i+1} of {total_files} files.", end="\r")
    print()  # print a newline character to move the cursor to the next line
    return {size: paths for size, paths in duplicates.items() if len(paths) > 1}


def remove_duplicates(duplicates):
    """
    Removes all duplicate files in the given dictionary of duplicates, except for the first one in each group.
    """
    for size, paths in duplicates.items():
        for path in paths[1:]:
            os.remove(path)


if __name__ == "__main__":
    main()
