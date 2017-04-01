import unittest
from src import process_log

class TestStringMethods(unittest.TestCase):

    def test_update(self):
        d = {'a': 1}
        process_log.update(d, 'a')
        self.assertEqual(d['a'], 2)

if __name__ == '__main__':
    unittest.main()
