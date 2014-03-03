try:
    import house_password
except ImportError:
    raise SystemExit('Could not find house_password.py. Does it exist?')

import unittest

class MostWantedTests(unittest.TestCase):
    def setUp(self):
        self.h = house_password.HousePwd()

    def test_first(self):
        self.assertEqual(
            False,
            self.h.checkio(u'A1213pokl')
        )

    def test_second(self):
        self.assertEqual(
            True,
            self.h.checkio(u'bAse730onE4')
        )

    def test_third(self):
        self.assertEqual(
            False,
            self.h.checkio(u'asasasasasasasaas')
        )

    def test_fourth(self):
        self.assertEqual(
            False,
            self.h.checkio(u'QWERTYqwerty')
        )

    def test_fifth(self):
        self.assertEqual(
            False,
            self.h.checkio(u'123456123456')
        )

    def test_fifth(self):
        self.assertEqual(
            False,
            self.h.checkio(u'123456123456')
        )

    def test_sixth(self):
        self.assertEqual(
            True,
            self.h.checkio(u'QwErTy911poqqqq')
        )

if __name__ == '__main__':
    unittest.main()
