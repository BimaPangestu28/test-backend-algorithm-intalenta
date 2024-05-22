import unittest
from merge_intervals import MergeIntervals


class TestMergeIntervals(unittest.TestCase):
    def test_merge_intervals(self):
        merger = MergeIntervals([[0, 300], [600, 1200], [3500, 6000]], 400)
        self.assertEqual(merger.merge(), [[0, 1200], [3500, 6000]])

        merger = MergeIntervals([[0, 300], [600, 1200], [3500, 6000]], 100)
        self.assertEqual(merger.merge(), [[0, 300], [600, 1200], [3500, 6000]])

        merger = MergeIntervals([[0, 300], [600, 1200], [3500, 6000]], 2500)
        self.assertEqual(merger.merge(), [[0, 6000]])


if __name__ == "__main__":
    unittest.main()
