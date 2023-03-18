import os
import filecmp
from tempfile import TemporaryDirectory
from unittest.mock import patch
from main import get_files, get_duplicates, remove_duplicates


def test_get_files():
    with TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, "subdir1"))
        os.makedirs(os.path.join(tmpdir, "subdir2"))
        with open(os.path.join(tmpdir, "file1.txt"), "w") as f:
            f.write("test")
        with open(os.path.join(tmpdir, "subdir1", "file2.txt"), "w") as f:
            f.write("test")
        with open(os.path.join(tmpdir, "subdir2", "file3.png"), "w") as f:
            f.write("test")
        files = get_files(tmpdir, ".txt")
        assert len(files) == 2
        assert os.path.join(tmpdir, "file1.txt") in files
        assert os.path.join(tmpdir, "subdir1", "file2.txt") in files


def test_get_duplicates():
    with TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, "file1.txt"), "w") as f1, open(
            os.path.join(tmpdir, "file2.txt"), "w"
        ) as f2, open(os.path.join(tmpdir, "file3.txt"), "w") as f3:
            f1.write("test")
            f2.write("test")
            f3.write("test2")
        files = [
            os.path.join(tmpdir, "file1.txt"),
            os.path.join(tmpdir, "file2.txt"),
            os.path.join(tmpdir, "file3.txt"),
        ]
        duplicates = get_duplicates(files)
        assert len(duplicates) == 1
        assert os.path.getsize(os.path.join(tmpdir, "file1.txt")) in duplicates
        assert (
            os.path.join(tmpdir, "file1.txt")
            in duplicates[os.path.getsize(os.path.join(tmpdir, "file1.txt"))]
        )
        assert (
            os.path.join(tmpdir, "file2.txt")
            in duplicates[os.path.getsize(os.path.join(tmpdir, "file1.txt"))]
        )


def test_remove_duplicates():
    with TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, "file1.txt"), "w") as f1, open(
            os.path.join(tmpdir, "file2.txt"), "w"
        ) as f2, open(os.path.join(tmpdir, "file3.txt"), "w") as f3:
            f1.write("test")
            f2.write("test")
            f3.write("test2")
        files = [
            os.path.join(tmpdir, "file1.txt"),
            os.path.join(tmpdir, "file2.txt"),
            os.path.join(tmpdir, "file3.txt"),
        ]
        duplicates = get_duplicates(files)
        with patch("os.remove") as mock_remove:
            remove_duplicates(duplicates)
            assert mock_remove.call_count == 1
            assert mock_remove.call_args_list[0][0][0] in [
                os.path.join(tmpdir, "file2.txt"),
                os.path.join(tmpdir, "file1.txt")
            ]

