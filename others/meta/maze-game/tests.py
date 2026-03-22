import unittest

from maze_runner import MazeRunner

# ------------------------------------------------------------------ #
# Test mazes                                                           #
# ------------------------------------------------------------------ #

# 6x6: S at (1,1), E at (4,4), items at (3,1) and (3,4)
#   ######
#   #S...#
#   #.##.#
#   #I..I#
#   #...E#
#   ######
SIMPLE_MAZE = [
    "######",
    "#S...#",
    "#.##.#",
    "#I..I#",
    "#...E#",
    "######",
]

# Walls completely cut off S from E
#   #####
#   #S.##
#   #####
#   ##E.#
#   #####
BLOCKED_MAZE = [
    "#####",
    "#S.##",
    "#####",
    "##E.#",
    "#####",
]

# 6x5: S at (1,1), E at (4,2), items at (2,2) and (3,3)
#   #####
#   #S..#
#   #.I.#
#   #..I#
#   #.E.#
#   #####
ITEMS_MAZE = [
    "#####",
    "#S..#",
    "#.I.#",
    "#..I#",
    "#.E.#",
    "#####",
]


# ------------------------------------------------------------------ #
# Part 1 — is_passable                                                #
# ------------------------------------------------------------------ #


class TestIsPassable(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = MazeRunner.from_strings(SIMPLE_MAZE)

    def test_start_cell_is_passable(self) -> None:
        self.assertTrue(self.runner.is_passable((1, 1)))

    def test_end_cell_is_passable(self) -> None:
        self.assertTrue(self.runner.is_passable((4, 4)))

    def test_open_cell_is_passable(self) -> None:
        self.assertTrue(self.runner.is_passable((1, 2)))

    def test_item_cell_is_passable(self) -> None:
        self.assertTrue(self.runner.is_passable((3, 1)))

    def test_wall_is_not_passable(self) -> None:
        self.assertFalse(self.runner.is_passable((0, 0)))

    def test_interior_wall_is_not_passable(self) -> None:
        self.assertFalse(self.runner.is_passable((2, 2)))

    def test_out_of_bounds_is_not_passable(self) -> None:
        self.assertFalse(self.runner.is_passable((-1, 0)))
        self.assertFalse(self.runner.is_passable((99, 99)))


# ------------------------------------------------------------------ #
# Part 2 — get_neighbors                                              #
# ------------------------------------------------------------------ #


class TestGetNeighbors(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = MazeRunner.from_strings(SIMPLE_MAZE)

    def test_corner_cell_has_two_passable_neighbors(self) -> None:
        # (1,1)=S — left and top are walls; right=(1,2) and down=(2,1)
        neighbors = set(self.runner.get_neighbors((1, 1)))
        self.assertEqual(neighbors, {(1, 2), (2, 1)})

    def test_open_cell_all_four_passable(self) -> None:
        # (3,2) is surrounded by open/item cells on all sides
        neighbors = set(self.runner.get_neighbors((3, 2)))
        self.assertEqual(neighbors, {(3, 1), (3, 3), (4, 2)})
        # (2,2) is a wall, so only 3 neighbors

    def test_wall_cell_has_no_neighbors(self) -> None:
        # A wall cell returns no passable neighbors
        neighbors = self.runner.get_neighbors((0, 0))
        self.assertEqual(neighbors, [])

    def test_neighbors_exclude_diagonal(self) -> None:
        # Movement is strictly orthogonal — diagonals must not appear
        neighbors = set(self.runner.get_neighbors((1, 1)))
        self.assertNotIn((2, 2), neighbors)


# ------------------------------------------------------------------ #
# Part 3 — find_shortest_path                                         #
# ------------------------------------------------------------------ #


class TestFindShortestPath(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = MazeRunner.from_strings(SIMPLE_MAZE)

    def test_same_position_returns_singleton(self) -> None:
        self.assertEqual(self.runner.find_shortest_path((1, 1), (1, 1)), [(1, 1)])

    def test_adjacent_cells(self) -> None:
        path = self.runner.find_shortest_path((1, 1), (1, 2))
        self.assertEqual(path, [(1, 1), (1, 2)])

    def test_shortest_path_length(self) -> None:
        # Both routes from S=(1,1) to E=(4,4) require 7 steps (6 moves)
        path = self.runner.find_shortest_path((1, 1), (4, 4))
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 7)

    def test_path_endpoints(self) -> None:
        path = self.runner.find_shortest_path((1, 1), (4, 4))
        self.assertIsNotNone(path)
        self.assertEqual(path[0], (1, 1))
        self.assertEqual(path[-1], (4, 4))

    def test_path_is_valid_walk(self) -> None:
        """Each consecutive pair in the path must be orthogonal neighbors."""
        path = self.runner.find_shortest_path((1, 1), (4, 4))
        self.assertIsNotNone(path)
        for i in range(len(path) - 1):
            r1, c1 = path[i]
            r2, c2 = path[i + 1]
            manhattan = abs(r2 - r1) + abs(c2 - c1)
            self.assertEqual(
                manhattan, 1, f"Non-adjacent step: {path[i]} → {path[i+1]}"
            )

    def test_no_path_returns_none(self) -> None:
        blocked = MazeRunner.from_strings(BLOCKED_MAZE)
        self.assertIsNone(blocked.find_shortest_path((1, 1), (3, 2)))

    def test_path_uses_items_maze(self) -> None:
        items_runner = MazeRunner.from_strings(ITEMS_MAZE)
        path = items_runner.find_shortest_path((1, 1), (4, 2))
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 5)  # 5 nodes = 4 moves


# ------------------------------------------------------------------ #
# Part 4 — count_reachable_cells                                      #
# ------------------------------------------------------------------ #


class TestCountReachableCells(unittest.TestCase):
    def test_all_cells_reachable_in_simple_maze(self) -> None:
        runner = MazeRunner.from_strings(SIMPLE_MAZE)
        # 14 non-wall cells, all connected from S
        self.assertEqual(runner.count_reachable_cells((1, 1)), 14)

    def test_blocked_maze_only_reaches_two_cells(self) -> None:
        runner = MazeRunner.from_strings(BLOCKED_MAZE)
        # S=(1,1) and (1,2) are the only reachable cells
        self.assertEqual(runner.count_reachable_cells((1, 1)), 2)

    def test_start_included_in_count(self) -> None:
        runner = MazeRunner.from_strings(SIMPLE_MAZE)
        count = runner.count_reachable_cells((1, 1))
        self.assertGreaterEqual(count, 1, "Start cell itself must be counted")

    def test_wall_start_returns_zero(self) -> None:
        runner = MazeRunner.from_strings(SIMPLE_MAZE)
        self.assertEqual(runner.count_reachable_cells((0, 0)), 0)

    def test_isolated_cell_returns_one(self) -> None:
        # A single open cell surrounded by walls
        solo = MazeRunner.from_strings(["###", "#S#", "###"])
        self.assertEqual(solo.count_reachable_cells((1, 1)), 1)


# ------------------------------------------------------------------ #
# Part 5 — collect_items                                              #
# ------------------------------------------------------------------ #


class TestCollectItems(unittest.TestCase):
    def test_items_returned_in_bfs_order(self) -> None:
        # In SIMPLE_MAZE, (3,1) is 2 hops from S, (3,4) is 5 hops — (3,1) first
        runner = MazeRunner.from_strings(SIMPLE_MAZE)
        items = runner.collect_items((1, 1))
        self.assertEqual(items[0], (3, 1), "(3,1) is closer and must appear first")
        self.assertEqual(items[1], (3, 4))

    def test_all_items_collected(self) -> None:
        runner = MazeRunner.from_strings(SIMPLE_MAZE)
        self.assertEqual(len(runner.collect_items((1, 1))), 2)

    def test_items_maze_order(self) -> None:
        # (2,2) is 2 hops from S; (3,3) is 4 hops
        runner = MazeRunner.from_strings(ITEMS_MAZE)
        items = runner.collect_items((1, 1))
        self.assertEqual(items, [(2, 2), (3, 3)])

    def test_no_items_returns_empty_list(self) -> None:
        no_items = MazeRunner.from_strings(["#####", "#S.E#", "#####"])
        self.assertEqual(no_items.collect_items((1, 1)), [])

    def test_unreachable_items_not_collected(self) -> None:
        # Item exists but is walled off from S
        walled_item = MazeRunner.from_strings(
            ["######", "#S###", "######", "##I##", "######"]
        )
        self.assertEqual(walled_item.collect_items((1, 1)), [])


if __name__ == "__main__":
    unittest.main()
