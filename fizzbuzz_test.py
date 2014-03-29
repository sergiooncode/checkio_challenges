try:
    import fizzbuzz
except ImportError:
    raise SystemExit('Could not find fizzbuzz.py. Does it exist?')

import unittest

class FizzbuzzTests(unittest.TestCase):
    def setUp(self):
        self.f = fizzbuzz.Fizzbuzz()

    def test_15divby3and5(self):
        self.assertEqual(
            "Fizz Buzz",
            self.f.checkio(15)
        )

    def test_6divby3(self):
        self.assertEqual(
            "Fizz",
            self.f.checkio(6)
        )

    def test_5divby5(self):
        self.assertEqual(
            "Buzz",
            self.f.checkio(5)
        )

    def test_7notdiv3and5(self):
        self.assertEqual(
            "7",
            self.f.checkio(7)
        )

if __name__ == '__main__':
    unittest.main()

    #     assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    # assert checkio(6) == "Fizz", "6 is divisible by 3"
    # assert checkio(5) == "Buzz", "5 is divisible by 5"
    # assert checkio(7) == "7", "7 is not divisible by 3 or 5"