import unittest
from sorted_set import SortedSet


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        s = SortedSet([])
        # self.assert_equal(True, False)  # add assertion here

    def test_sequence(self):
        s = SortedSet([7, 8, 3, 1])

    def test_with_duplicates(self):
        s = SortedSet([8, 8, 8, 8])


if __name__ == '__main__':
    unittest.main()
