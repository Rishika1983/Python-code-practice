import unittest
import SmallestEven


class TestSmallerEven(unittest.TestCase):
    def test1(self):
        num1 = 2
        num2 = 4
        result = SmallestEven.lesser_of_two_even(num1,num2)
        self.assertEqual(result, 2)

    def test2(self):
        num1 = 2
        num2 = 7
        result = SmallestEven.lesser_of_two_even(num1,num2)
        self.assertEqual(result, 7)

    def test3(self):
        num1 = 9
        num2 = 7
        result = SmallestEven.lesser_of_two_even(num1,num2)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
