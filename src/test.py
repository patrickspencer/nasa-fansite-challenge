import unittest
import process_log

class TestStringMethods(unittest.TestCase):

    def test_update_hash(self):
        d = {'a': 1}
        process_log.update_hash(d, 'a')
        self.assertEqual(d['a'], 2)

    def test_min_heap(self):
        min_heap = {"blah": 0, "another": 1}
        m = min(min_heap, key=min_heap.get)
        self.assertEqual("blah", m)
        self.assertNotEqual("another", m)

    def test_min_key(self):
        d = {'a': 10,
             'b': 4,
             'c': 2,
             'd': 8,
             'e': 7,
             'f': 5}

        self.assertEqual(process_log.min_key(d), 'c')
        self.assertNotEqual(process_log.min_key(d), 'a')

    def test_min_value(self):
        d = {'a': 10,
             'b': 4,
             'c': 2,
             'd': 8,
             'e': 7,
             'f': 5}

        self.assertEqual(process_log.min_value(d), 2)
        self.assertNotEqual(process_log.min_key(d), 9)


if __name__ == '__main__':
    unittest.main()
