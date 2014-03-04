try:
    import non_unique
except ImportError:
    raise SystemExit('Could not find non_unique.py. Does it exist?')

import unittest

class NonUniqueTests(unittest.TestCase):
    def setUp(self):
        self.n = non_unique.NonUnique()

    def test_isalist(self):
        self.assertEqual(
            True,
            isinstance(self.n.checkio([1]), list)
        )

    def test_first(self):
        self.assertEqual(
            [1, 3, 1, 3],
            self.n.checkio([1, 2, 3, 1, 3])
        )

    def test_second(self):
        self.assertEqual(
            [],
            self.n.checkio([1, 2, 3, 4, 5])
        )

    def test_third(self):
        self.assertEqual(
            [5, 5, 5, 5, 5],
            self.n.checkio([5, 5, 5, 5, 5])
        )

    def test_fourth(self):
        self.assertEqual(
            [10, 9, 10, 10, 9],
            self.n.checkio([10, 9, 10, 10, 9, 8])
        )

if __name__ == '__main__':
    unittest.main()
