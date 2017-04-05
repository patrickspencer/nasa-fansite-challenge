# -*- coding: utf-8 -*-

"""
process_log.py
~~~~~~~~~~~~~~
Part of the Nasa Fansite Anaslytics Challenge, an Insight Data Engineer
programming challenge.

process_log.py is the main file for processing logs

:copyright: (c) 2017 by Patrick Spencer.
:license: Don't touch my stuff. But seriously, a restrictive EULA. See LICENSE
    for more details.
"""

import re
import lib
import time
import pprint
import models
import settings

pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":
    start_time = time.time()

    # log_file_name = 'log_head_100000.txt'
    # log_file = settings.load_log_file(log_file_name)
    # requests = lib.read_file(log_file)

    # print("--- Starting frequency count ---")
    #
    # hosts = lib.create_host_freq_hash(requests)
    # lib.write_file(lib.top_freq(hosts),'hosts.txt')
    #
    # print("--- Time to find top frequencies: %s secs ---" % (time.time() - start_time))

    # start_time_2 = time.time()
    #
    # print("--- Starting most used resource ---")
    #
    # bytes_dict = lib.create_bytes_dict(log_file)
    # top_bytes = lib.get_top_dict_values(bytes_dict, 10)
    # pp.pprint(top_bytes)
    # lib.write_file(top_bytes,'resources.txt', include_values=True)
    #
    # print("--- Time to find most demanding resources: %s secs ---" % (time.time() - start_time_2))

    fixture = settings.load_fixture('block_list_test.txt')
    requests = lib.read_file(fixture)
    print(lib.check_for_mult_logins(requests))
    #
    # pp.pprint(block_list)

        # last = int(r.date.timestamp())

    print("--- Total run time: %s seconds ---" % (time.time() - start_time))
