try:
    import medianchio
except ImportError:
    raise SystemExit('Could not find medianchio.py. Does it exist?')

import unittest

class MedianchioTests(unittest.TestCase):
    def setUp(self):
        self.md = medianchio.Median()

    def test_sortedlist(self):
        self.assertEqual(
            3,
            self.md.checkio([1, 2, 3, 4, 5])
        )

    def test_notsortedlist(self):
        self.assertEqual(
            3,
            self.md.checkio([3, 1, 2, 5, 3])
        )

    def test_notanavg(self):
        self.assertEqual(
            2,
            self.md.checkio([1, 300, 2, 200, 1])
        )

    def test_evenlength(self):
        self.assertEqual(
            12.5,
            self.md.checkio([3, 6, 20, 99, 10, 15])
        )


if __name__ == '__main__':
    unittest.main()