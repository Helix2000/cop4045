"""Demonstrate recursive folder sizes and large-file searches for Problem 6."""
# Part F
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
find_large_files = _problem6.find_large_files


def _format_files(files: list[File]) -> str:
    """Format files as readable names and byte sizes for terminal output."""
    return ", ".join(f"{file.name} ({file.size()} bytes)" for file in files) or "None"


def main() -> None:
    """Build a nested folder tree and print size and threshold search results."""
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

    print("Folder hierarchy: homework/documents/coursework/submissions")
    print(f"Total size of outermost folder '{root.name}': {root.size()} bytes")

    for minimum_size in (100, 50):
        matching_files: list[File] = find_large_files(root, minimum_size)
        print(
            f"Files at least {minimum_size} bytes: "
            f"{_format_files(matching_files)}"
        )


if __name__ == "__main__":
    main()
