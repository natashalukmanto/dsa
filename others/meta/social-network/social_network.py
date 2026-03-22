from __future__ import annotations

from collections import deque
from typing import Dict, List, Optional, Set

from friend_graph import FriendGraph
from user import User


class SocialNetwork:
    """Friend-graph–backed social network with recommendation and path-finding.

    Starter code (already provided):
        add_user, add_friendship, get_friends

    Your tasks — implement the four methods marked below:
        Part 1 → get_mutual_friends
        Part 2 → suggest_friends
        Part 3 → shortest_path
        Part 4 → find_influencers
    """

    def __init__(self) -> None:
        self.graph = FriendGraph()

    # ------------------------------------------------------------------ #
    # Starter code — provided, do not modify                              #
    # ------------------------------------------------------------------ #

    def add_user(self, user_id: str, name: str) -> None:
        """Register a new user in the network."""
        self.graph.add_user(User(user_id=user_id, name=name))

    def add_friendship(self, user_id_a: str, user_id_b: str) -> None:
        """Create a bidirectional friendship between two existing users."""
        self.graph.add_edge(user_id_a, user_id_b)

    def get_friends(self, user_id: str) -> List[str]:
        """Return a sorted list of direct friends of user_id."""
        return sorted(self.graph.get_neighbors(user_id))

    # ------------------------------------------------------------------ #
    # Part 1                                                              #
    # ------------------------------------------------------------------ #

    def get_mutual_friends(self, user_id_a: str, user_id_b: str) -> Set[str]:
        """Return the set of users who are friends with both user_id_a and user_id_b.

        Excludes user_id_a and user_id_b themselves from the result even if
        they appear in each other's friend lists.

        Example (see build_sample_network in tests.py for the topology):
            get_mutual_friends("alice", "charlie") == {"bob"}
        """
        res = set()
        
        user_id_a_neighbors = self.graph.get_neighbors(user_id_a)
        user_id_b_neighbors = self.graph.get_neighbors(user_id_b)
        
        for neighbor in user_id_a_neighbors:
            if neighbor in user_id_b_neighbors: 
                res.add(neighbor)
        
        return res

    # ------------------------------------------------------------------ #
    # Part 2                                                              #
    # ------------------------------------------------------------------ #

    def suggest_friends(self, user_id: str, limit: int = 5) -> List[str]:
        """Return up to `limit` friend suggestions for user_id.

        A suggestion is any user who:
          - is NOT already a direct friend of user_id
          - is NOT user_id themselves
          - shares at least one mutual friend with user_id
            (i.e. is a friend-of-a-friend)

        Suggestions are ranked by:
          1. number of mutual friends with user_id (descending)
          2. user_id string (ascending) to break ties

        Example:
            suggest_friends("alice")  →  ["charlie", "eve"]
                # both share 1 mutual friend (bob); charlie < eve alphabetically
        """
        direct_friends = self.graph.get_neighbors(user_id)
        mutual_count: Dict[str, int] = {}
        
        for friend_id in direct_friends:
            for fof in self.graph.get_neighbors(friend_id):
                if fof != user_id and fof not in direct_friends:
                    mutual_count[fof] = mutual_count.get(fof, 0) + 1
        
        # Sorting
        return sorted(mutual_count, key=lambda uid: (-mutual_count[uid], uid))[:limit]
          
    # ------------------------------------------------------------------ #
    # Part 3                                                              #
    # ------------------------------------------------------------------ #

    def shortest_path(self, start_id: str, end_id: str) -> Optional[List[str]]:
        """Find the shortest chain of friendships between two users using BFS.

        Returns the list of user IDs forming the path from start_id to end_id
        (both endpoints included), or None if the two users are not connected.

        If start_id == end_id, return [start_id].

        Example:
            shortest_path("alice", "frank")  →  ["alice", "bob", "eve", "frank"]
        """
        if start_id == end_id:
            return [start_id]
        
        queue = deque([[start_id]])
        visited = set()
        
        while queue:
            path = queue.popleft() # queue = [[alice, charlie], [...], [alice, bob, eve]]
            for neighbor in self.graph.get_neighbors(path[-1]):
                if neighbor == end_id:
                    return path + [neighbor]
                if neighbor not in visited:
                    queue.append(path + [neighbor])
                    visited.add(neighbor)
        
        return None
          
    # ------------------------------------------------------------------ #
    # Part 4                                                              #
    # ------------------------------------------------------------------ #

    def find_influencers(self, k: int) -> List[str]:
        """Return the top-k users ranked by number of direct friends (degree).

        Ties are broken by user_id ascending (lexicographic).
        If k exceeds the number of users, return all users.

        Example:
            find_influencers(1)  →  ["bob"]          # 3 friends
            find_influencers(3)  →  ["bob", "charlie", "eve"]
                # charlie and eve both have 2 friends; charlie < eve
        """
        return sorted(self.graph.all_user_ids(), key=lambda uid: (-len(self.graph.get_neighbors(uid)), uid))[:k]
