import os
import lib
import time
import models
import settings
import unittest
from datetime import datetime

if __name__ == '__main__':
    start_time = time.time()

    print("*** Starting to load file ***\n")

    log_file_name = 'log.txt'
    log_file = settings.load_log_file(log_file_name)
    requests = lib.read_file(log_file)

    print("--- Time it took to load file: %s secs ---" % (time.time() - start_time))

    print("--- Starting frequency count ---")

    hosts = lib.create_host_freq_hash(requests)
    lib.write_file(lib.top_freq(hosts),'hosts.txt')

    print("--- Ending frequency count. Time elapsed: %s secs ---" % (time.time() - start_time))

    start_time_2 = time.time()

    print("--- Starting search for most used resources ---")

    bytes_dict = lib.create_bytes_dict(log_file)
    top_bytes = lib.get_top_dict_values(bytes_dict, 10)
    lib.write_file(top_bytes,'resources.txt', include_values=False)

    print("--- Ending search for most demanded resources. Time elapsed: %s secs ---" % (time.time() - start_time_2))

    start_time_3 = time.time()

    print("--- Starting search for failed login attempts ---")

    fixture = settings.load_fixture('block_list_test.txt')
    requests = lib.read_file(fixture)
    lib.write_blocked(lib.check_for_mult_logins(requests))

    print("--- Ending search for failed login attempts. Time elapsed: %s secs ---" % (time.time() - start_time_3))

    start_time_4 = time.time()

    print("--- Starting search for busiest hours ---")

    intervals = lib.find_busiest_intervals(requests, time_interval = 3600, n = 11)
    lib.write_busiest_times(intervals)

    print("--- Endign search for busiest hours. Time elapsed: %s secs ---" % (time.time() - start_time_4))

    print("--- Total run time: %s seconds ---" % (time.time() - start_time))
