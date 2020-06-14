import unittest
from src.calc import add, sub, mult, div


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.__x, self.__y = 3, 2

    def test_add(self):
        self.assertEqual(add(self.__x, self.__y), 5)

    def test_sub(self):
        self.assertEqual(sub(self.__x, self.__y), 1)
        self.assertEqual(sub(self.__y, self.__x), -1)

    def test_mult(self):
        self.assertEqual(mult(self.__x, self.__y), 6)

    def test_div(self):
        self.assertEqual(div(self.__x, self.__y), 1.5)


if __name__ == "__main__":
    unittest.main()
