import unittest
import guess


class MyTestCase(unittest.TestCase):
    def test_run_guess1(self):
        self.assertFalse(guess.run_guess(2, 3))

    def test_run_guess2(self):
        self.assertTrue(guess.run_guess(3, 3))

    def test_run_guess3(self):
        self.assertFalse(guess.run_guess("20", 3))


if __name__ == '__main__':
    unittest.main()
