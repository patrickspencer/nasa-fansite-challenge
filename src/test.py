import os
import lib
import models
import settings
import unittest

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
        request_str2 = 'klothos.crl.research.digital.com - - [10/Jul/1995:16:45:50 -0400] "" 400 -'
        r = models.Request(request_str2)
        self.assertEqual(r.host, 'klothos.crl.research.digital.com')
        self.assertEqual(r.date_str, '10/Jul/1995:16:45:50 -0400')
        self.assertEqual(r.method, '')
        self.assertEqual(r.resource, '')
        self.assertEqual(r.protocol, '')
        self.assertEqual(r.response, '400')
        self.assertEqual(r.bytes, 0)
        request_str2 = 'klothos.crl.research.digital.com - - [10/Jul/1995:16:45:50 -0400] "POST /history/apollo/" 400 -'
        r = models.Request(request_str2)
        self.assertEqual(r.host, 'klothos.crl.research.digital.com')
        self.assertEqual(r.date_str, '10/Jul/1995:16:45:50 -0400')
        self.assertEqual(r.method, 'POST')
        self.assertEqual(r.resource, '/history/apollo/')
        self.assertEqual(r.protocol, '')
        self.assertEqual(r.response, '400')
        self.assertEqual(r.bytes, 0)

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
        self.assertEqual(r.protocol, '')

        pass

class TestSettings(unittest.TestCase):

    def test_log_input_dir(self):
        log_file = settings.load_log_file('log.txt')
        self.assertTrue(os.path.exists(settings.log_input_dir))

    def test_fixture_dir(self):
        fixture = settings.load_fixture('domain_freq.txt')
        fake_fixture = settings.load_fixture('not_a_file.txt')
        self.assertTrue(os.path.exists(fixture))
        self.assertFalse(os.path.exists(fake_fixture))

class TestLib(unittest.TestCase):

    def test_update_hash_freq(self):
        d = {'a': 1}
        lib.update_hash_freq(d, 'a')
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

        self.assertEqual(lib.min_key(d), 'c')
        self.assertNotEqual(lib.min_key(d), 'a')

    def test_min_value(self):
        d = {'a': 10,
             'b': 4,
             'c': 2,
             'd': 8,
             'e': 7,
             'f': 5}
        self.assertEqual(lib.min_value(d), 2)
        self.assertNotEqual(lib.min_key(d), 9)

    def test_read_file(self):
        pass

    def test_top_freq(self):
        domain_freq = {
             'host_a': 5,
             'host_b': 4,
             'host_c': 2,
             'host_d': 1,
             'host_e': 7,
             'host_f': 6,
             'host_g': 1,
             'host_h': 8,
             'host_i': 1,
             'host_j': 3,
             'host_k': 12,
             'host_l': 9,
             'host_m': 11,
             'host_n': 14}
        top = lib.top_freq(domain_freq)
        self.assertEqual(len(top), 10)
        self.assertEqual(top['host_n'], 14)
        self.assertEqual(top['host_k'], 12)
        self.assertEqual(top['host_l'], 9)
        self.assertEqual(top['host_b'], 4)
        self.assertEqual(top['host_j'], 3)
        self.assertFalse('host_d' in top)
        self.assertFalse('host_g' in top)
        self.assertFalse('host_i' in top)

    def test_create_host_freq_hash(self):
        """I know it's the same as test_top_freq but it gives me extra piece of
        mind to know I'm testing this function
        """
        freq_file = settings.load_fixture('domain_freq.txt')
        requests = lib.read_file(freq_file)
        freqs = lib.create_host_freq_hash(requests)
        self.assertEqual(freqs['host_a'], 5)
        self.assertEqual(freqs['host_b'], 4)
        self.assertEqual(freqs['host_c'], 2)
        self.assertEqual(freqs['host_d'], 1)
        self.assertEqual(freqs['host_e'], 7)
        self.assertEqual(freqs['host_f'], 6)
        self.assertEqual(freqs['host_g'], 1)
        self.assertEqual(freqs['host_h'], 8)
        self.assertEqual(freqs['host_i'], 1)
        self.assertEqual(freqs['host_j'], 3)
        self.assertEqual(freqs['host_k'], 12)
        self.assertEqual(freqs['host_l'], 9)
        self.assertEqual(freqs['host_m'], 11)
        self.assertEqual(freqs['host_n'], 14)

    def test_remove_min_value(self):
        arr = [804626197, 804626198, 804626201]
        lib.remove_min(arr)
        self.assertEqual(arr, [804626198, 804626201])

    def update_block_list(self):
        last_logins = [804612566, 804612567, 804612568]
        block_list = {}
        lib.update_block_list(block_list, 'host1', max(las_logins))
        self.assertTrue(804612568 in last_logins)

    def update_401_d(self):
        last_logins = [804612566, 804612567, 804612568]
        block_list = {}
        lib.update_block_list(block_list, 'host1', max(las_logins))
        self.assertTrue(804612568 in last_logins)

    def test_check_for_mult_logins(self):
        fixture = settings.load_fixture('block_list_test.txt')
        requests = lib.read_file(fixture)
        failed_logins = lib.check_for_mult_logins(requests)
        self.assertTrue(failed_logins[0] == '207.109.29.70 - - [01/Jul/1995:01:28:41 -0400] "POST /login HTTP/1.0" 401 1420')
        self.assertTrue(failed_logins[1] == '207.109.29.70 - - [01/Jul/1995:01:35:14 -0400] "POST /login HTTP/1.0" 401 1420')
        self.assertTrue(failed_logins[2] == '207.246.17.94 - - [01/Jul/1995:02:51:27 -0400] "POST /login HTTP/1.0" 401 1420')

if __name__ == '__main__':
    unittest.main()
