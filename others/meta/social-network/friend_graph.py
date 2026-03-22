from __future__ import annotations

from typing import Dict, List, Optional, Set

from user import User


class FriendGraph:
    """Undirected graph representing friendships between users.

    Uses an adjacency-set representation so that neighbor lookups,
    insertions, and membership checks are all O(1) average case.
    """

    def __init__(self) -> None:
        self._users: Dict[str, User] = {}
        self._adjacency: Dict[str, Set[str]] = {}

    def add_user(self, user: User) -> None:
        """Register a user. No-op if the user already exists."""
        if user.user_id not in self._users:
            self._users[user.user_id] = user
            self._adjacency[user.user_id] = set()

    def add_edge(self, user_id_a: str, user_id_b: str) -> None:
        """Create a bidirectional friendship edge.

        Both users must already be registered in the graph.
        Adding a self-loop or a duplicate edge is silently ignored.
        """
        if user_id_a not in self._users or user_id_b not in self._users:
            raise ValueError(
                f"Both users must exist before adding a friendship: "
                f"'{user_id_a}', '{user_id_b}'"
            )
        if user_id_a == user_id_b:
            return
        self._adjacency[user_id_a].add(user_id_b)
        self._adjacency[user_id_b].add(user_id_a)

    def get_neighbors(self, user_id: str) -> Set[str]:
        """Return a snapshot of the direct friends of user_id."""
        if user_id not in self._adjacency:
            raise KeyError(f"User '{user_id}' not found in graph.")
        return set(self._adjacency[user_id])

    def has_user(self, user_id: str) -> bool:
        return user_id in self._users

    def get_user(self, user_id: str) -> Optional[User]:
        return self._users.get(user_id)

    def all_user_ids(self) -> List[str]:
        """Return all registered user IDs in insertion order."""
        return list(self._users.keys())
