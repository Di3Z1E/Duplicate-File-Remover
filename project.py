import os


def get_files(path):
    """Returns a list of all files in a directory."""
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            files.append(full_path)
    return files


def find_duplicates(files):
    """Returns a list of all files with duplicate sizes."""
    sizes = {}
    for file in files:
        size = os.path.getsize(file)
        if size not in sizes:
            sizes[size] = [file]
        else:
            sizes[size].append(file)
    return [group for group in sizes.values() if len(group) > 1]


def remove_duplicates(duplicates):
    """Removes duplicate files."""
    for group in duplicates:
        for file in group[1:]:
            os.remove(file)


if __name__ == "__main__":
    path = input("Enter the path to the directory to search: ")
    files = get_files(path)
    duplicates = find_duplicates(files)
    if duplicates:
        print("Duplicate files found:")
        for group in duplicates:
            print("-" * 40)
            for file in group:
                print(file)
        response = input("Do you want to delete the duplicate files? (y/n) ")
        if response.lower() == "y":
            remove_duplicates(duplicates)
            print("Duplicate files deleted.")
        else:
            print("No files were deleted.")
    else:
        print("No duplicate files found.")
