import os
import models
import settings
import unittest
import process_log

class TestModels(unittest.TestCase):

    def test_request_init(self):
        request_str = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245'
        r = models.Request(request_str)
        self.assertEqual(r.host, '199.72.81.55')
        self.assertEqual(r.date_str, '01/Jul/1995:00:00:01 -0400')
        self.assertEqual(r.method, 'GET')
        self.assertEqual(r.resource, '/history/apollo/')
        self.assertEqual(r.protocol, 'HTTP/1.0')
        self.assertEqual(r.response, '200')
        self.assertEqual(r.bytes, 6245)

    def test_request_init2(self):
        """Test if a request which didn't download anything returns zero bytes"""
        request_str = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 404 -'
        r = models.Request(request_str)
        self.assertEqual(r.bytes, 0)

    def test_request_init3(self):
        """Test whether the regex can parse a request string that does not have
        a transefer protocol at the end of its resource part"""
        request_str = '215.145.83.92 - - [01/Jul/1995:00:00:41 -0400] "GET /shuttle/missions/sts-71/movies/movies.html" 200 3089'
        r = models.Request(request_str)
        self.assertEqual(r.protocol, None)

        pass

    def test_fixture_dir(self):
        fixture = settings.load_fixture('domain_freq.txt')
        fake_fixture = settings.load_fixture('not_a_file.txt')
        self.assertTrue(os.path.exists(fixture))
        self.assertFalse(os.path.exists(fake_fixture))

class TestSettings(unittest.TestCase):

    def test_log_input_dir(self):
        log_file = settings.load_log_file('log.txt')
        self.assertTrue(os.path.exists(settings.log_input_dir))

    def test_fixture_dir(self):
        fixture = settings.load_fixture('domain_freq.txt')
        fake_fixture = settings.load_fixture('not_a_file.txt')
        self.assertTrue(os.path.exists(fixture))
        self.assertFalse(os.path.exists(fake_fixture))

class TestProcessLog(unittest.TestCase):

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

    def test_read_file(self):
        pass

    def test_top_freq(self):
        domain_freq = {
             'domain_a': 5,
             'domain_b': 4,
             'domain_c': 2,
             'domain_d': 1,
             'domain_e': 7,
             'domain_f': 6,
             'domain_g': 1,
             'domain_h': 8,
             'domain_i': 1,
             'domain_j': 3,
             'domain_k': 12,
             'domain_l': 9,
             'domain_m': 11,
             'domain_n': 14}
        top = process_log.top_freq(domain_freq)
        self.assertEqual(len(top), 10)
        self.assertEqual(top['domain_n'], 14)
        self.assertEqual(top['domain_k'], 12)
        self.assertEqual(top['domain_l'], 9)
        self.assertEqual(top['domain_b'], 4)
        self.assertEqual(top['domain_j'], 3)
        self.assertFalse('domain_d' in top)
        self.assertFalse('domain_g' in top)
        self.assertFalse('domain_i' in top)

if __name__ == '__main__':
    unittest.main()
