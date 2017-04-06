import os
import lib
import time
import models
import settings
import unittest
from datetime import datetime

if __name__ == '__main__':
    start_time = time.time()

    print("*** Starting to load file (this will take a couple of minutes)***\n")

    log_file_name = 'log.txt'
    log_file = settings.load_log_file(log_file_name)
    requests = lib.read_file(log_file)

    print("--- Time it took to load file: %s secs ---" % (time.time() - start_time))

    print("--- Starting frequency count ---")

    # Make copy of list. This is resource intensive but necessary
    r1 = list(requests)
    hosts = lib.create_host_freq_hash(r1)
    lib.write_file(lib.top_freq(hosts),'hosts.txt')

    print("--- Ending frequency count. Time elapsed: %s secs ---" % (time.time() - start_time))
    # delete r1 from memory
    del r1[:]

    start_time_2 = time.time()

    print("--- Starting search for most used resources ---")

    bytes_dict = lib.create_bytes_dict(log_file)
    top_bytes = lib.get_top_dict_values(bytes_dict, 10)
    lib.write_file(top_bytes,'resources.txt', include_values=False)

    print("--- Ending search for most demanded resources. Time elapsed: %s secs ---" % (time.time() - start_time_2))

    start_time_3 = time.time()

    print("--- Starting search for failed login attempts ---")

    r3 = list(requests)
    lib.write_blocked(lib.check_for_mult_logins(r3))

    print("--- Ending search for failed login attempts. Time elapsed: %s secs ---" % (time.time() - start_time_3))
    # delete r3 from memory
    del r3[:]

    start_time_4 = time.time()

    print("--- Starting search for busiest hours ---")

    r4 = list(requests)
    intervals = lib.find_busiest_intervals(r4, time_interval = 3600, n = 11)
    lib.write_busiest_times(intervals)

    print("--- Ending search for busiest hours. Time elapsed: %s secs ---" % (time.time() - start_time_4))

    print("--- Total run time: %s seconds ---" % (time.time() - start_time))
