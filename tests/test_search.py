import unittest
from bfs import bfs
from dfs import dfs
from graph import build_graph
from profile import profile_search

class SearchTests(unittest.TestCase):
    def test_graph_size(self):
        self.assertEqual(len(build_graph(1000)), 1000)

    def test_bfs_shortest_path(self):
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = bfs(0, 3, graph)
        self.assertTrue(result["found"])
        self.assertEqual(result["path"], [0, 1, 3])

    def test_dfs_finds_goal(self):
        graph = {0: [1, 2], 1: [3], 2: [], 3: []}
        result = dfs(0, 3, graph)
        self.assertTrue(result["found"])
        self.assertEqual(result["path"][0], 0)
        self.assertEqual(result["path"][-1], 3)

    def test_unreachable_goal(self):
        graph = {0: [1], 1: [], 2: []}
        self.assertFalse(bfs(0, 2, graph)["found"])
        self.assertFalse(dfs(0, 2, graph)["found"])

    def test_missing_nodes(self):
        graph = {0: [1], 1: []}
        self.assertFalse(bfs(5, 1, graph)["found"])
        self.assertFalse(dfs(0, 5, graph)["found"])

    def test_profile_metrics(self):
        metrics = profile_search(bfs, 0, 19, build_graph(20), repeat=2)
        self.assertTrue(metrics["result"]["found"])
        self.assertGreaterEqual(metrics["best_ms"], 0)
        self.assertGreaterEqual(metrics["worst_ms"], metrics["best_ms"])
        self.assertGreaterEqual(metrics["average_ms"], 0)

if __name__ == "__main__":
    unittest.main()
