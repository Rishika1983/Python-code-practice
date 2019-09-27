import unittest
import RemovePunctuation


class TestRmPunct(unittest.TestCase):

    def test1(self):
        str = 'ahdjadh£naddska%zcm'
        result = RemovePunctuation.remove_punctuation(str)
        self.assertEqual(result,'ahdjadh naddska zcm')


if __name__ == '__main__':
    unittest.main()