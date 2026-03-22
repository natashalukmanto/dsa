from __future__ import annotations

from typing import List, Optional, Tuple

from fs_node import FSNode


class FileSystem:
    """Tree-backed file system with path navigation and disk-usage queries.

    Paths use Unix-style forward slashes. The root is always "/".
    Empty path components (from leading/trailing slashes) are ignored.

    Starter code (already provided):
        __init__

    Your tasks — implement the five methods marked below:
        Part 1 → get_node
        Part 2 → list_directory
        Part 3 → total_size
        Part 4 → search
        Part 5 → find_largest_files
    """

    def __init__(self, root: FSNode) -> None:
        self._root = root

    # ------------------------------------------------------------------ #
    # Part 1                                                              #
    # ------------------------------------------------------------------ #

    def get_node(self, path: str) -> Optional[FSNode]:
        """Navigate to path and return the FSNode at that location.

        Returns None if any segment of the path does not exist or if
        traversal passes through a file node (files have no children).
        get_node("/") always returns the root.

        Example (see build_sample_fs in tests.py for the tree):
            get_node("/home/alice")            →  <FSNode name="alice" is_dir=True>
            get_node("/home/alice/resume.pdf") →  <FSNode name="resume.pdf" size=1024>
            get_node("/home/nonexistent")      →  None
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 2                                                              #
    # ------------------------------------------------------------------ #

    def list_directory(self, path: str) -> List[str]:
        """Return a sorted list of child names for the directory at path.

        Raises ValueError if path does not exist or is a file.

        Example:
            list_directory("/home")        →  ["alice", "bob"]
            list_directory("/home/alice")  →  ["notes.txt", "resume.pdf"]
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 3                                                              #
    # ------------------------------------------------------------------ #

    def total_size(self, path: str) -> int:
        """Return the total byte size of all files under path.

        For a file, returns its own size.
        For a directory, recursively sums the sizes of all descendant files.

        Raises ValueError if path does not exist.

        Example:
            total_size("/home/alice")  →  1280   # 1024 + 256
            total_size("/home")        →  5504   # 1024 + 256 + 4096 + 128
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 4                                                              #
    # ------------------------------------------------------------------ #

    def search(self, name: str) -> List[str]:
        """Find all nodes (files or directories) whose name exactly matches.

        Returns full absolute paths sorted lexicographically.
        Searches the entire tree starting from root.

        Example:
            search("config.txt")  →  ["/home/bob/config.txt"]
            search("config")      →  ["/etc/config"]   # directory match
            search("missing")     →  []
        """
        raise NotImplementedError

    # ------------------------------------------------------------------ #
    # Part 5                                                              #
    # ------------------------------------------------------------------ #

    def find_largest_files(self, k: int) -> List[Tuple[str, int]]:
        """Return the top-k largest files as (absolute_path, size) tuples.

        Directories are excluded. Ties broken by path ascending.
        If k exceeds the total number of files, return all files.

        Example:
            find_largest_files(3)  →  [
                ("/home/bob/photo.jpg",   4096),
                ("/tmp/cache.tmp",        2048),
                ("/home/alice/resume.pdf", 1024),
            ]
        """
        raise NotImplementedError
