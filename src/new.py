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

    log_file_name = 'log_head_1000.txt'
    log_file = settings.load_log_file(log_file_name)
    requests = lib.read_file(log_file)

    print("Time it took to load file: %s secs" % (time.time() - start_time))

    start_time_1 = time.time()


    start_time_4 = time.time()

    print("--- Starting to finding busiest hours ---")

    intervals = lib.find_busiest_intervals(requests, time_interval = 5, n = 11)
    lib.write_busiest_times(intervals)

    print("--- Time to find failed login attempts: %s secs ---" % (time.time() - start_time_4))
