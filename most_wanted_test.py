try:
    import most_wanted
except ImportError:
    raise SystemExit('Could not find most_wanted.py. Does it exist?')

import unittest

class MostWantedTests(unittest.TestCase):
    def setUp(self):
        self.m = most_wanted.MostWanted()

    def test_lorem(self):
        self.assertEqual(
            "m",
            self.m.checkio(u"Lorem ipsum dolor sit amet")
        )

    def test_hello(self):
        self.assertEqual(
            "l",
            self.m.checkio(u"Hello World!")
        )

    def test_oumostwanted(self):
        self.assertEqual(
            "o",
            self.m.checkio(u"How do you do?")
        )

    def test_allonlyonce(self):
        self.assertEqual(
            "e",
            self.m.checkio(u"One")
        )

    def test_lotsofzeros(self):
        self.assertEqual(
            "m",
            self.m.checkio(u"Lorem ipsum dolor sit amet 00000000000000000000000")
        )

if __name__ == '__main__':
    unittest.main()

#     assert checkio(u"Lorem ipsum dolor sit amet 00000000000000000000000")