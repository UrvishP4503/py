import unittest
import main


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print(f"About to test somethings and for that doing a setup")

    def test_do_stuff1(self):
        result = main.do_stuff(1)
        self.assertEqual(result, 69)

    def test_do_stuff2(self):
        para = "uwu"
        result = main.do_stuff(para)
        self.assertIsInstance(result, ValueError)

    def test_do_more_stuff1(self):
        result = main.do_more_stuff(1, 2)
        self.assertEqual(result, 2)

    def test_do_more_stuff2(self):
        """If this run you are dead"""
        result = main.do_more_stuff('e', 4)
        self.assertEqual(result, "eeee")

    def tearDown(self) -> None:
        print(f"cleaning up things")

# 'python3 -m unittest -v' gives more info about test and also shows docstrings


if __name__ == '__main__':
    unittest.main()
