import os
from project import find_duplicates, remove_duplicates


def test_find_duplicates(tmp_path):
    """Test that find_duplicates returns the correct list of duplicate files."""
    # create some files with duplicate sizes
    path = str(tmp_path)
    with open(os.path.join(path, "file1.txt"), "w") as f:
        f.write("Hello, world!")
    with open(os.path.join(path, "file2.txt"), "w") as f:
        f.write("Goodbye, world!")
    with open(os.path.join(path, "file3.txt"), "w") as f:
        f.write("Hello, world!")
    # call find_duplicates and check the result
    files = [os.path.join(path, f) for f in os.listdir(path)]
    duplicates = find_duplicates(files)
    assert len(duplicates) == 1
    assert len(duplicates[0]) == 2
    assert os.path.basename(duplicates[0][0]) == "file1.txt"
    assert os.path.basename(duplicates[0][1]) == "file3.txt"


def test_remove_duplicates(tmp_path):
    """Test that remove_duplicates removes the correct files."""
    # create some files with duplicate sizes
    path = str(tmp_path)
    with open(os.path.join(path, "file1.txt"), "w") as f:
        f.write("Hello, world!")
    with open(os.path.join(path, "file2.txt"), "w") as f:
        f.write("Goodbye, world!")
    with open(os.path.join(path, "file3.txt"), "w") as f:
        f.write("Hello, world!")
    # call find_duplicates and remove_duplicates and check the result
    files = [os.path.join(path, f) for f in os.listdir(path)]
    duplicates = find_duplicates(files)
    remove_duplicates(duplicates)
    assert len(os.listdir(path)) == 2
    assert "file1.txt" in os.listdir(path)
    assert "file2.txt" in os.listdir(path)
