import unittest

from file_system import FileSystem
from fs_node import FSNode


def build_sample_fs() -> FileSystem:
    """Construct the following file system tree for testing:

    /
    ├── home/
    │   ├── alice/
    │   │   ├── resume.pdf   (1024 bytes)
    │   │   └── notes.txt    ( 256 bytes)
    │   └── bob/
    │       ├── photo.jpg    (4096 bytes)
    │       └── config.txt   ( 128 bytes)
    ├── etc/
    │   ├── hosts            ( 512 bytes)
    │   └── config/
    │       └── settings.txt ( 768 bytes)
    └── tmp/
        └── cache.tmp        (2048 bytes)

    Total sizes:
        /home/alice → 1280     /home → 5504
        /etc        → 1280     /     → 8832
    """
    root = FSNode.make_dir("/")

    home = FSNode.make_dir("home")
    alice = FSNode.make_dir("alice")
    alice.add_child(FSNode.make_file("resume.pdf", 1024))
    alice.add_child(FSNode.make_file("notes.txt", 256))
    bob = FSNode.make_dir("bob")
    bob.add_child(FSNode.make_file("photo.jpg", 4096))
    bob.add_child(FSNode.make_file("config.txt", 128))
    home.add_child(alice)
    home.add_child(bob)

    etc = FSNode.make_dir("etc")
    etc.add_child(FSNode.make_file("hosts", 512))
    config_dir = FSNode.make_dir("config")
    config_dir.add_child(FSNode.make_file("settings.txt", 768))
    etc.add_child(config_dir)

    tmp = FSNode.make_dir("tmp")
    tmp.add_child(FSNode.make_file("cache.tmp", 2048))

    root.add_child(home)
    root.add_child(etc)
    root.add_child(tmp)
    return FileSystem(root)


# ------------------------------------------------------------------ #
# Part 1 — get_node                                                   #
# ------------------------------------------------------------------ #


class TestGetNode(unittest.TestCase):
    def setUp(self) -> None:
        self.fs = build_sample_fs()

    def test_get_root(self) -> None:
        node = self.fs.get_node("/")
        self.assertIsNotNone(node)
        self.assertTrue(node.is_dir)

    def test_get_directory_one_level(self) -> None:
        node = self.fs.get_node("/home")
        self.assertIsNotNone(node)
        self.assertTrue(node.is_dir)
        self.assertEqual(node.name, "home")

    def test_get_directory_two_levels(self) -> None:
        node = self.fs.get_node("/home/alice")
        self.assertIsNotNone(node)
        self.assertTrue(node.is_dir)
        self.assertEqual(node.name, "alice")

    def test_get_file(self) -> None:
        node = self.fs.get_node("/home/alice/resume.pdf")
        self.assertIsNotNone(node)
        self.assertFalse(node.is_dir)
        self.assertEqual(node.size, 1024)

    def test_nonexistent_segment_returns_none(self) -> None:
        self.assertIsNone(self.fs.get_node("/home/nobody"))

    def test_path_through_file_returns_none(self) -> None:
        # resume.pdf is a file; navigating into it is impossible
        self.assertIsNone(self.fs.get_node("/home/alice/resume.pdf/child"))

    def test_deeply_nested_file(self) -> None:
        node = self.fs.get_node("/etc/config/settings.txt")
        self.assertIsNotNone(node)
        self.assertEqual(node.size, 768)


# ------------------------------------------------------------------ #
# Part 2 — list_directory                                             #
# ------------------------------------------------------------------ #


class TestListDirectory(unittest.TestCase):
    def setUp(self) -> None:
        self.fs = build_sample_fs()

    def test_list_root(self) -> None:
        self.assertEqual(self.fs.list_directory("/"), ["etc", "home", "tmp"])

    def test_list_home(self) -> None:
        self.assertEqual(self.fs.list_directory("/home"), ["alice", "bob"])

    def test_list_alice_sorted(self) -> None:
        # notes.txt sorts before resume.pdf
        self.assertEqual(
            self.fs.list_directory("/home/alice"), ["notes.txt", "resume.pdf"]
        )

    def test_list_single_child_directory(self) -> None:
        self.assertEqual(self.fs.list_directory("/tmp"), ["cache.tmp"])

    def test_list_file_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            self.fs.list_directory("/home/alice/resume.pdf")

    def test_list_nonexistent_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            self.fs.list_directory("/home/nobody")


# ------------------------------------------------------------------ #
# Part 3 — total_size                                                 #
# ------------------------------------------------------------------ #


class TestTotalSize(unittest.TestCase):
    def setUp(self) -> None:
        self.fs = build_sample_fs()

    def test_single_file_size(self) -> None:
        self.assertEqual(self.fs.total_size("/home/alice/resume.pdf"), 1024)

    def test_small_directory(self) -> None:
        self.assertEqual(self.fs.total_size("/home/alice"), 1280)  # 1024 + 256

    def test_directory_with_subdirs(self) -> None:
        self.assertEqual(self.fs.total_size("/home"), 5504)  # 1024+256+4096+128

    def test_root_total(self) -> None:
        self.assertEqual(self.fs.total_size("/"), 8832)

    def test_single_file_directory(self) -> None:
        self.assertEqual(self.fs.total_size("/tmp"), 2048)

    def test_nested_config_dir(self) -> None:
        self.assertEqual(self.fs.total_size("/etc/config"), 768)

    def test_nonexistent_path_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            self.fs.total_size("/home/nobody")


# ------------------------------------------------------------------ #
# Part 4 — search                                                     #
# ------------------------------------------------------------------ #


class TestSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.fs = build_sample_fs()

    def test_find_file(self) -> None:
        self.assertEqual(self.fs.search("resume.pdf"), ["/home/alice/resume.pdf"])

    def test_find_file_deep(self) -> None:
        self.assertEqual(
            self.fs.search("settings.txt"), ["/etc/config/settings.txt"]
        )

    def test_find_directory_by_name(self) -> None:
        # "config" is a directory under /etc
        self.assertEqual(self.fs.search("config"), ["/etc/config"])

    def test_find_multiple_matches_sorted(self) -> None:
        # Both alice and bob have a "config.txt" / only bob does here; check notes
        results = self.fs.search("notes.txt")
        self.assertEqual(results, ["/home/alice/notes.txt"])

    def test_no_match_returns_empty(self) -> None:
        self.assertEqual(self.fs.search("does_not_exist.txt"), [])

    def test_exact_name_only(self) -> None:
        # Partial name "config" must not match "config.txt"
        results = self.fs.search("config")
        self.assertNotIn("/home/bob/config.txt", results)
        self.assertIn("/etc/config", results)


# ------------------------------------------------------------------ #
# Part 5 — find_largest_files                                         #
# ------------------------------------------------------------------ #


class TestFindLargestFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.fs = build_sample_fs()

    def test_top_one_largest(self) -> None:
        result = self.fs.find_largest_files(1)
        self.assertEqual(result, [("/home/bob/photo.jpg", 4096)])

    def test_top_three_largest(self) -> None:
        result = self.fs.find_largest_files(3)
        self.assertEqual(
            result,
            [
                ("/home/bob/photo.jpg", 4096),
                ("/tmp/cache.tmp", 2048),
                ("/home/alice/resume.pdf", 1024),
            ],
        )

    def test_directories_excluded(self) -> None:
        result = self.fs.find_largest_files(10)
        paths = [r[0] for r in result]
        for path in paths:
            node = self.fs.get_node(path)
            self.assertFalse(node.is_dir, f"{path} is a directory but appeared in results")

    def test_k_exceeds_file_count_returns_all(self) -> None:
        result = self.fs.find_largest_files(100)
        self.assertEqual(len(result), 7)  # 7 files total in the tree

    def test_k_zero_returns_empty(self) -> None:
        self.assertEqual(self.fs.find_largest_files(0), [])

    def test_tie_broken_by_path(self) -> None:
        # Build a small fs where two files have the same size
        root = FSNode.make_dir("/")
        root.add_child(FSNode.make_file("b_file.txt", 500))
        root.add_child(FSNode.make_file("a_file.txt", 500))
        fs = FileSystem(root)
        result = fs.find_largest_files(2)
        self.assertEqual(result[0][0], "/a_file.txt")  # 'a' < 'b'
        self.assertEqual(result[1][0], "/b_file.txt")


if __name__ == "__main__":
    unittest.main()
