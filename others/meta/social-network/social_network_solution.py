"""Temporary solution to verify all tests pass. Delete after verification."""
from __future__ import annotations

from collections import deque
from typing import Dict, List, Optional, Set

from friend_graph import FriendGraph
from user import User


class SocialNetwork:
    def __init__(self) -> None:
        self.graph = FriendGraph()

    def add_user(self, user_id: str, name: str) -> None:
        self.graph.add_user(User(user_id=user_id, name=name))

    def add_friendship(self, user_id_a: str, user_id_b: str) -> None:
        self.graph.add_edge(user_id_a, user_id_b)

    def get_friends(self, user_id: str) -> List[str]:
        return sorted(self.graph.get_neighbors(user_id))

    def get_mutual_friends(self, user_id_a: str, user_id_b: str) -> Set[str]:
        return self.graph.get_neighbors(user_id_a) & self.graph.get_neighbors(user_id_b)

    def suggest_friends(self, user_id: str, limit: int = 5) -> List[str]:
        direct_friends = self.graph.get_neighbors(user_id)
        mutual_count: Dict[str, int] = {}
        for friend_id in direct_friends:
            for fof in self.graph.get_neighbors(friend_id):
                if fof != user_id and fof not in direct_friends:
                    mutual_count[fof] = mutual_count.get(fof, 0) + 1
        return sorted(mutual_count, key=lambda uid: (-mutual_count[uid], uid))[:limit]

    def shortest_path(self, start_id: str, end_id: str) -> Optional[List[str]]:
        if start_id == end_id:
            return [start_id]
        queue: deque[List[str]] = deque([[start_id]])
        visited = {start_id}
        while queue:
            path = queue.popleft()
            for neighbor in self.graph.get_neighbors(path[-1]):
                if neighbor == end_id:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None

    def find_influencers(self, k: int) -> List[str]:
        return sorted(
            self.graph.all_user_ids(),
            key=lambda uid: (-len(self.graph.get_neighbors(uid)), uid),
        )[:k]
