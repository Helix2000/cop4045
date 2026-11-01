"""Problem 6: entries, folders, recursive searches, tests, and demonstrations."""
# Jose Marrero Z23816617

from __future__ import annotations

import sys
import unittest
from typing import Optional


STUDENT_ID: str = "Z23816617"  # Replace this value if submitting for another student.


class Entry:
    """Base class for an item with a name and an optional parent entry."""

    def __init__(self, name: str, parent: Optional[Entry] = None) -> None:
        """Create an entry with its name and parent."""
        self.name: str = name
        self._parent: Optional[Entry] = parent

    def parent(self) -> Optional[Entry]:
        """Return this entry's parent, or None if it has no parent."""
        return self._parent

    def absolute_path(self) -> list[Entry]:
        """Return this entry and its ancestors, ending with the root entry.

        The list starts with this entry and follows parent references upward.
        """
        parent: Optional[Entry] = self.parent()
        if parent is None:
            return [self]
        return [self] + parent.absolute_path()

    def size(self) -> int:
        """Return this entry's size in bytes."""
        raise NotImplementedError("Subclasses must implement size().")


class File(Entry):
    """An entry that represents a file with a nonnegative byte size."""

    def __init__(
        self,
        name: str,
        bytes_used: int,
        parent: Optional[Entry] = None,
    ) -> None:
        """Create a file, rejecting a negative byte count."""
        if bytes_used < 0:
            raise ValueError("bytes_used must be nonnegative.")

        super().__init__(name, parent)
        self.bytes_used: int = bytes_used

    def size(self) -> int:
        """Return the size of the file in bytes."""
        return self.bytes_used

# Jose Marrero Z23816617
class Folder(Entry):
    """An entry that contains child entries, including files and folders."""

    def __init__(self, name: str, parent: Optional[Entry] = None) -> None:
        """Create an empty folder with a name and an optional parent."""
        super().__init__(name, parent)
        self._children: list[Entry] = []

    def add(self, entry: Entry) -> None:
        """Add an entry as a child and set its parent to this folder."""
        self._children.append(entry)
        entry._parent = self

    def children(self) -> tuple[Entry, ...]:
        """Return the folder's children as a tuple."""
        return tuple(self._children)

    def size(self) -> int:
        """Return the total size of files in this folder and nested folders."""
        return sum(entry.size() for entry in self._children)


def find_large_files(entry: Entry, minimum_size: int) -> list[File]:
    """Find files at least ``minimum_size`` bytes within an entry.

    If ``entry`` is a file, it is returned when its size meets the threshold.
    If it is a folder, its children are searched recursively, including files
    in nested folders. The returned list follows the folder child order.
    """
    if isinstance(entry, File):
        return [entry] if entry.size() >= minimum_size else []

    if isinstance(entry, Folder):
        large_files: list[File] = []
        for child in entry.children():
            large_files.extend(find_large_files(child, minimum_size))
        return large_files

    return []


class FindLargeFilesTests(unittest.TestCase):
    """Tests for finding files by size in entries and nested folders."""

    def test_file_entry_at_or_above_threshold(self) -> None:
        """Return a file when its size equals or exceeds the threshold."""
        file_at_threshold: File = File("exact.bin", 10)
        larger_file: File = File("large.bin", 15)

        self.assertEqual(find_large_files(file_at_threshold, 10), [file_at_threshold])
        self.assertEqual(find_large_files(larger_file, 10), [larger_file])

    def test_file_entry_below_threshold(self) -> None:
        """Return no files when a file entry is smaller than the threshold."""
        small_file: File = File("small.bin", 9)

        self.assertEqual(find_large_files(small_file, 10), [])
    # Jose Marrero ZNUMBER: Z23816617
    def test_nested_folders_and_inclusive_threshold(self) -> None:
        """Find qualifying files recursively and preserve child order."""
        root: Folder = Folder("root")
        nested: Folder = Folder("nested")
        exact_file: File = File("exact.bin", 10)
        small_file: File = File("small.bin", 4)
        large_file: File = File("large.bin", 20)
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
        root: Folder = Folder("root")
        empty_file: File = File("empty.bin", 0)
        root.add(empty_file)

        self.assertEqual(find_large_files(root, 0), [empty_file])


class AbsolutePathTests(unittest.TestCase):
    """Tests for paths from entries up to their root entry."""

    def test_root_entry_path_contains_only_root(self) -> None:
        """Return a one-entry path for a root with no parent."""
        root: Folder = Folder("root")

        path: list[Entry] = root.absolute_path()

        self.assertEqual(len(path), 1)
        self.assertIs(path[0], root)

    def test_nested_file_path_ends_at_root(self) -> None:
        """Return a nested file, its parent folder, and the root in order."""
        root: Folder = Folder("root")
        nested: Folder = Folder("nested")
        file: File = File("report.bin", 12)
        root.add(nested)
        nested.add(file)

        path: list[Entry] = file.absolute_path()

        self.assertEqual(len(path), 3)
        self.assertIs(path[0], file)
        self.assertIs(path[1], nested)
        self.assertIs(path[2], root)


def _format_files(files: list[File]) -> str:
    """Format files as readable names and byte sizes for terminal output."""
    return ", ".join(f"{file.name} ({file.size()} bytes)" for file in files) or "None"
#Jose Marrero ZNUMBER: Z23816617

def demonstrate_part_f() -> None:
    """Print recursive folder size and large-file search results."""
    root: Folder = Folder("homework")
    documents: Folder = Folder("documents")
    coursework: Folder = Folder("coursework")
    submissions: Folder = Folder("submissions")

    root.add(File("readme.txt", 40))
    root.add(documents)
    documents.add(File("notes.txt", 80))
    documents.add(coursework)
    coursework.add(File("draft.py", 120))
    coursework.add(submissions)
    submissions.add(File("final.py", 250))
    submissions.add(File("diagram.png", 60))

    print("Part F demonstration")
    print("Folder hierarchy: homework/documents/coursework/submissions")
    print(f"Total size of outermost folder '{root.name}': {root.size()} bytes")

    for minimum_size in (100, 50):
        matching_files: list[File] = find_large_files(root, minimum_size)
        print(
            f"Files at least {minimum_size} bytes: "
            f"{_format_files(matching_files)}"
        )


def _format_path(entry: Entry) -> str:
    """Format an entry's absolute path from the entry up to the root."""
    return " -> ".join(path_entry.name for path_entry in entry.absolute_path())


def demonstrate_part_g() -> None:
    """Print absolute paths for a deeply nested folder and file."""
    root: Folder = Folder("homework")
    documents: Folder = Folder("documents")
    coursework: Folder = Folder("coursework")
    submissions: Folder = Folder("submissions")
    final_file: File = File("final.py", 250)

    root.add(File("readme.txt", 40))
    root.add(documents)
    documents.add(File("notes.txt", 80))
    documents.add(coursework)
    coursework.add(File("draft.py", 120))
    coursework.add(submissions)
    submissions.add(final_file)
    submissions.add(File("diagram.png", 60))

    print("Part G demonstration (paths from entry to root)")
    print(f"Folder '{submissions.name}': {_format_path(submissions)}")
    print(f"File '{final_file.name}': {_format_path(final_file)}")

# Jose Marrero ZNUMBER: Z23816617
def run_unit_tests() -> unittest.result.TestResult:
    """Run the six Part E unit tests and return their result."""
    suite: unittest.TestSuite = unittest.TestSuite()
    loader: unittest.TestLoader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(FindLargeFilesTests))
    suite.addTests(loader.loadTestsFromTestCase(AbsolutePathTests))
    runner: unittest.TextTestRunner = unittest.TextTestRunner(
        stream=sys.stdout,
        verbosity=2,
    )
    return runner.run(suite)


def main() -> None:
    """Print the student ID, run both demos, and execute all six unit tests."""
    print(f"FAU Student ID: {STUDENT_ID}")
    print()
    demonstrate_part_f()
    print()
    demonstrate_part_g()
    print()
    result: unittest.result.TestResult = run_unit_tests()
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == "__main__":
    main()
