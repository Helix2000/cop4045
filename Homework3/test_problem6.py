"""Unit tests for Problem 6's path and large-file functions."""
#Part E
import importlib.machinery
import importlib.util
from pathlib import Path
from types import ModuleType
import unittest


def _load_problem6() -> ModuleType:
    """Load the extensionless Problem 6 source file as a Python module."""
    source_path: Path = Path(__file__).with_name("problem6")
    loader: importlib.machinery.SourceFileLoader = (
        importlib.machinery.SourceFileLoader("problem6_module", str(source_path))
    )
    spec = importlib.util.spec_from_loader(loader.name, loader)
    if spec is None:
        raise ImportError(f"Unable to load Problem 6 source from {source_path}.")

    module: ModuleType = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


_problem6: ModuleType = _load_problem6()
Entry = _problem6.Entry
File = _problem6.File
Folder = _problem6.Folder
find_large_files = _problem6.find_large_files


class FindLargeFilesTests(unittest.TestCase):
    """Tests for finding files by size in entries and nested folders."""

    def test_file_entry_at_or_above_threshold(self) -> None:
        """Return a file when its size equals or exceeds the threshold."""
        file_at_threshold = File("exact.bin", 10)
        larger_file = File("large.bin", 15)

        self.assertEqual(find_large_files(file_at_threshold, 10), [file_at_threshold])
        self.assertEqual(find_large_files(larger_file, 10), [larger_file])

    def test_file_entry_below_threshold(self) -> None:
        """Return no files when a file entry is smaller than the threshold."""
        small_file = File("small.bin", 9)

        self.assertEqual(find_large_files(small_file, 10), [])

    def test_nested_folders_and_inclusive_threshold(self) -> None:
        """Find qualifying files recursively and preserve child order."""
        root = Folder("root")
        nested = Folder("nested")
        exact_file = File("exact.bin", 10)
        small_file = File("small.bin", 4)
        large_file = File("large.bin", 20)
        root.add(exact_file)
        root.add(nested)
        nested.add(small_file)
        nested.add(large_file)

        self.assertEqual(
            find_large_files(root, 10),
            [exact_file, large_file],
        )

    def test_root_folder_with_zero_threshold(self) -> None:
        """Include zero-byte files beneath the root when the threshold is zero."""
        root = Folder("root")
        empty_file = File("empty.bin", 0)
        root.add(empty_file)

        self.assertEqual(find_large_files(root, 0), [empty_file])


class AbsolutePathTests(unittest.TestCase):
    """Tests for paths from entries up to their root entry."""

    def test_root_entry_path_contains_only_root(self) -> None:
        """Return a one-entry path for a root with no parent."""
        root = Folder("root")

        path: list[Entry] = root.absolute_path()

        self.assertEqual(len(path), 1)
        self.assertIs(path[0], root)

    def test_nested_file_path_ends_at_root(self) -> None:
        """Return a nested file, its parent folder, and the root in order."""
        root = Folder("root")
        nested = Folder("nested")
        file = File("report.bin", 12)
        root.add(nested)
        nested.add(file)

        path: list[Entry] = file.absolute_path()

        self.assertEqual(len(path), 3)
        self.assertIs(path[0], file)
        self.assertIs(path[1], nested)
        self.assertIs(path[2], root)


if __name__ == "__main__":
    unittest.main()
