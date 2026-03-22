from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class FSNode:
    """A node in a file system tree, representing either a file or a directory.

    Files have a non-zero size and an empty children dict.
    Directories have size=0 and may have any number of named children.
    """

    name: str
    is_dir: bool
    size: int
    children: Dict[str, "FSNode"] = field(default_factory=dict)

    @classmethod
    def make_dir(cls, name: str) -> "FSNode":
        """Create a directory node with no children."""
        return cls(name=name, is_dir=True, size=0)

    @classmethod
    def make_file(cls, name: str, size: int) -> "FSNode":
        """Create a file node with the given byte size."""
        return cls(name=name, is_dir=False, size=size)

    def add_child(self, child: "FSNode") -> None:
        """Add a child node to this directory.

        Raises ValueError if this node is a file.
        """
        if not self.is_dir:
            raise ValueError(f"'{self.name}' is not a directory.")
        self.children[child.name] = child
