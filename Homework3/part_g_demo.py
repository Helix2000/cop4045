"""Demonstrate absolute paths for entries in the Part F folder hierarchy."""

import importlib.machinery
import importlib.util
from pathlib import Path
from types import ModuleType


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


def _format_path(entry: Entry) -> str:
    """Format an entry's absolute path from the entry up to the root."""
    return " -> ".join(path_entry.name for path_entry in entry.absolute_path())


def main() -> None:
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

    print("Absolute paths (entry to root):")
    print(f"Folder '{submissions.name}': {_format_path(submissions)}")
    print(f"File '{final_file.name}': {_format_path(final_file)}")


if __name__ == "__main__":
    main()
