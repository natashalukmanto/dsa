from __future__ import annotations

from typing import List, Optional, Tuple

from fs_node import FSNode


class FileSystem:
    def __init__(self, root: FSNode) -> None:
        self._root = root

    def get_node(self, path: str) -> Optional[FSNode]:
        parts = [p for p in path.split("/") if p]
        current = self._root
        for part in parts:
            if not current.is_dir or part not in current.children:
                return None
            current = current.children[part]
        return current

    def list_directory(self, path: str) -> List[str]:
        node = self.get_node(path)
        if node is None or not node.is_dir:
            raise ValueError(f"Not a directory: {path}")
        return sorted(node.children.keys())

    def total_size(self, path: str) -> int:
        node = self.get_node(path)
        if node is None:
            raise ValueError(f"Path not found: {path}")
        if not node.is_dir:
            return node.size
        total = 0
        stack = [node]
        while stack:
            current = stack.pop()
            if current.is_dir:
                stack.extend(current.children.values())
            else:
                total += current.size
        return total

    def search(self, name: str) -> List[str]:
        results: List[str] = []

        def dfs(node: FSNode, current_path: str) -> None:
            for child_name, child in sorted(node.children.items()):
                child_path = current_path + "/" + child_name
                if child_name == name:
                    results.append(child_path)
                if child.is_dir:
                    dfs(child, child_path)

        dfs(self._root, "")
        return results

    def find_largest_files(self, k: int) -> List[Tuple[str, int]]:
        all_files: List[Tuple[str, int]] = []

        def dfs(node: FSNode, current_path: str) -> None:
            for child_name, child in node.children.items():
                child_path = current_path + "/" + child_name
                if child.is_dir:
                    dfs(child, child_path)
                else:
                    all_files.append((child_path, child.size))

        dfs(self._root, "")
        return sorted(all_files, key=lambda x: (-x[1], x[0]))[:k]
