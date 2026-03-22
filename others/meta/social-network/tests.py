import unittest

from social_network import SocialNetwork


def build_sample_network() -> SocialNetwork:
    """Construct a small network for use across multiple test cases.

    Friendship topology (undirected edges):

        alice ── bob ── charlie ── diana
                  │
                 eve ── frank

    Adjacency summary:
        alice   : [bob]
        bob     : [alice, charlie, eve]
        charlie : [bob, diana]
        diana   : [charlie]
        eve     : [bob, frank]
        frank   : [eve]
    """
    sn = SocialNetwork()
    for uid, name in [
        ("alice", "Alice"),
        ("bob", "Bob"),
        ("charlie", "Charlie"),
        ("diana", "Diana"),
        ("eve", "Eve"),
        ("frank", "Frank"),
    ]:
        sn.add_user(uid, name)

    sn.add_friendship("alice", "bob")
    sn.add_friendship("bob", "charlie")
    sn.add_friendship("bob", "eve")
    sn.add_friendship("charlie", "diana")
    sn.add_friendship("eve", "frank")
    return sn


def build_disconnected_network() -> SocialNetwork:
    """Two isolated components: {alice, bob} and {charlie, diana}."""
    sn = SocialNetwork()
    for uid, name in [
        ("alice", "Alice"),
        ("bob", "Bob"),
        ("charlie", "Charlie"),
        ("diana", "Diana"),
    ]:
        sn.add_user(uid, name)
    sn.add_friendship("alice", "bob")
    sn.add_friendship("charlie", "diana")
    return sn


# ------------------------------------------------------------------ #
# Part 1 — get_mutual_friends                                         #
# ------------------------------------------------------------------ #


class TestGetMutualFriends(unittest.TestCase):
    def setUp(self) -> None:
        self.sn = build_sample_network()

    def test_returns_shared_friend(self) -> None:
        """alice and charlie share bob as a mutual friend."""
        self.assertEqual(self.sn.get_mutual_friends("alice", "charlie"), {"bob"})

    def test_returns_shared_friend_symmetric(self) -> None:
        """get_mutual_friends is symmetric: (a, b) == (b, a)."""
        self.assertEqual(
            self.sn.get_mutual_friends("alice", "charlie"),
            self.sn.get_mutual_friends("charlie", "alice"),
        )

    def test_no_mutual_friends(self) -> None:
        """diana and alice share no mutual friends."""
        self.assertEqual(self.sn.get_mutual_friends("alice", "diana"), set())

    def test_direct_friends_not_counted_as_mutual(self) -> None:
        """Mutual friends of alice and bob should not include alice or bob."""
        mutuals = self.sn.get_mutual_friends("alice", "bob")
        self.assertNotIn("alice", mutuals)
        self.assertNotIn("bob", mutuals)

    def test_multiple_mutual_friends(self) -> None:
        """Add an extra edge so bob and diana share both charlie and a new user."""
        sn = SocialNetwork()
        for uid, name in [("a", "A"), ("b", "B"), ("c", "C"), ("d", "D"), ("e", "E")]:
            sn.add_user(uid, name)
        # a and b both know c, d, e
        sn.add_friendship("a", "c")
        sn.add_friendship("a", "d")
        sn.add_friendship("a", "e")
        sn.add_friendship("b", "c")
        sn.add_friendship("b", "d")
        sn.add_friendship("b", "e")
        self.assertEqual(sn.get_mutual_friends("a", "b"), {"c", "d", "e"})


# ------------------------------------------------------------------ #
# Part 2 — suggest_friends                                            #
# ------------------------------------------------------------------ #


class TestSuggestFriends(unittest.TestCase):
    def setUp(self) -> None:
        self.sn = build_sample_network()

    def test_basic_suggestions_for_leaf_node(self) -> None:
        """alice → friends-of-bob that alice doesn't know yet."""
        suggestions = self.sn.suggest_friends("alice")
        # charlie and eve are both reachable through bob (1 mutual each)
        self.assertIn("charlie", suggestions)
        self.assertIn("eve", suggestions)

    def test_already_friends_not_suggested(self) -> None:
        """bob must not appear in alice's suggestions."""
        suggestions = self.sn.suggest_friends("alice")
        self.assertNotIn("bob", suggestions)

    def test_self_not_suggested(self) -> None:
        """alice must not suggest herself."""
        suggestions = self.sn.suggest_friends("alice")
        self.assertNotIn("alice", suggestions)

    def test_tie_broken_alphabetically(self) -> None:
        """charlie and eve both have 1 mutual friend with alice; charlie sorts first."""
        suggestions = self.sn.suggest_friends("alice")
        charlie_idx = suggestions.index("charlie")
        eve_idx = suggestions.index("eve")
        self.assertLess(charlie_idx, eve_idx)

    def test_limit_respected(self) -> None:
        """limit=1 should return exactly one suggestion."""
        suggestions = self.sn.suggest_friends("alice", limit=1)
        self.assertEqual(len(suggestions), 1)

    def test_higher_mutual_count_ranked_first(self) -> None:
        """User with more mutual friends should rank above users with fewer."""
        sn = SocialNetwork()
        # dave knows alice, bob, and charlie. george only knows alice.
        # So for zara, dave has 3 mutuals, george has 1.
        for uid, name in [
            ("zara", "Zara"), ("alice", "Alice"), ("bob", "Bob"),
            ("charlie", "Charlie"), ("dave", "Dave"), ("george", "George"),
        ]:
            sn.add_user(uid, name)
        sn.add_friendship("zara", "alice")
        sn.add_friendship("zara", "bob")
        sn.add_friendship("zara", "charlie")
        sn.add_friendship("dave", "alice")
        sn.add_friendship("dave", "bob")
        sn.add_friendship("dave", "charlie")
        sn.add_friendship("george", "alice")

        suggestions = sn.suggest_friends("zara")
        self.assertEqual(suggestions[0], "dave", "dave has 3 mutuals and should rank first")
        self.assertEqual(suggestions[1], "george", "george has 1 mutual and should rank second")

    def test_no_suggestions_when_isolated(self) -> None:
        """A user with no friends has no friend-of-friend suggestions."""
        sn = SocialNetwork()
        sn.add_user("solo", "Solo")
        self.assertEqual(sn.suggest_friends("solo"), [])


# ------------------------------------------------------------------ #
# Part 3 — shortest_path                                              #
# ------------------------------------------------------------------ #


class TestShortestPath(unittest.TestCase):
    def setUp(self) -> None:
        self.sn = build_sample_network()

    def test_same_user_returns_singleton(self) -> None:
        path = self.sn.shortest_path("alice", "alice")
        self.assertEqual(path, ["alice"])

    def test_direct_friends(self) -> None:
        path = self.sn.shortest_path("alice", "bob")
        self.assertEqual(path, ["alice", "bob"])

    def test_path_length_three(self) -> None:
        path = self.sn.shortest_path("alice", "charlie")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "alice")
        self.assertEqual(path[-1], "charlie")
        self.assertEqual(len(path), 3)

    def test_longer_path(self) -> None:
        """alice → frank requires traversing 4 nodes."""
        path = self.sn.shortest_path("alice", "frank")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "alice")
        self.assertEqual(path[-1], "frank")
        self.assertEqual(len(path), 4)

    def test_path_is_valid_chain(self) -> None:
        """Every consecutive pair in the returned path must be friends."""
        path = self.sn.shortest_path("alice", "diana")
        self.assertIsNotNone(path)
        for i in range(len(path) - 1):
            friends_of_current = self.sn.get_friends(path[i])
            self.assertIn(
                path[i + 1],
                friends_of_current,
                f"{path[i]} and {path[i+1]} are not friends.",
            )

    def test_no_path_in_disconnected_graph(self) -> None:
        sn = build_disconnected_network()
        self.assertIsNone(sn.shortest_path("alice", "charlie"))

    def test_path_is_bidirectional(self) -> None:
        """Path from a→b and b→a should have the same length."""
        path_ab = self.sn.shortest_path("alice", "frank")
        path_ba = self.sn.shortest_path("frank", "alice")
        self.assertIsNotNone(path_ab)
        self.assertIsNotNone(path_ba)
        self.assertEqual(len(path_ab), len(path_ba))


# ------------------------------------------------------------------ #
# Part 4 — find_influencers                                           #
# ------------------------------------------------------------------ #


class TestFindInfluencers(unittest.TestCase):
    def setUp(self) -> None:
        self.sn = build_sample_network()

    def test_top_one_influencer(self) -> None:
        """bob has 3 friends — the most in the network."""
        self.assertEqual(self.sn.find_influencers(1), ["bob"])

    def test_top_three_influencers(self) -> None:
        """bob (3), then charlie and eve (2 each, charlie < eve alphabetically)."""
        self.assertEqual(self.sn.find_influencers(3), ["bob", "charlie", "eve"])

    def test_tie_broken_alphabetically(self) -> None:
        """charlie and eve both have degree 2; charlie should come first."""
        top3 = self.sn.find_influencers(3)
        charlie_idx = top3.index("charlie")
        eve_idx = top3.index("eve")
        self.assertLess(charlie_idx, eve_idx)

    def test_k_exceeds_user_count_returns_all(self) -> None:
        """k larger than the network size returns all users."""
        result = self.sn.find_influencers(100)
        self.assertEqual(len(result), 6)

    def test_k_zero_returns_empty(self) -> None:
        self.assertEqual(self.sn.find_influencers(0), [])

    def test_full_ranking(self) -> None:
        """Full ranking from most to least connected, ties alphabetical."""
        result = self.sn.find_influencers(6)
        self.assertEqual(result[0], "bob")       # degree 3
        self.assertEqual(result[1], "charlie")   # degree 2
        self.assertEqual(result[2], "eve")       # degree 2
        # alice, diana, frank all have degree 1 — alphabetical
        self.assertEqual(result[3], "alice")
        self.assertEqual(result[4], "diana")
        self.assertEqual(result[5], "frank")


if __name__ == "__main__":
    unittest.main()
