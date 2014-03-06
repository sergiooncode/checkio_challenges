try:
    import hamming_dist
except ImportError:
    raise SystemExit('Could not find hamming_dist.py. Does it exist?')

import unittest

class HammDistTests(unittest.TestCase):
    def setUp(self):
        self.h = hamming_dist.HammDist()

    def test_first(self):
        self.assertEqual(
            3,
            self.h.checkio(117, 17)
        )

    def test_second(self):
        self.assertEqual(
            2,
            self.h.checkio(1, 2)
        )

    def test_third(self):
        self.assertEqual(
            5,
            self.h.checkio(16, 15)
        )

if __name__ == '__main__':
    unittest.main()

    #     assert checkio(117, 17) == 3, "First example"
#     assert checkio(1, 2) == 2, "Second example"
#     assert checkio(16, 15) == 5, "Third example"