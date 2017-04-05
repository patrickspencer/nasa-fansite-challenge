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
import datetime

if __name__ == "__main__":
    start_time = time.time()

    log_file_name = 'log_head_30.txt'
    log_file = settings.load_log_file(log_file_name)
    requests = lib.read_file(log_file)

    # for ts in top_ten:
    #     reconverted_stamp = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y:%H:%M:%S %z')
    #     print(str(ts) + ' <-> ' + str(reconverted_stamp) + ' <-> ' + str(top_ten[ts]))
    # top_ten_with_dates = {}
    # for timestamp in top_ten:
    #     dt = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%d/%m/%Y:%H:%M:%S %z')
    #     dt = dt + '-0400'
    #     top_ten_with_dates[dt] = top_ten[timestamp]
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(top_ten)
    # pp.pprint(top_ten_with_dates)
    # print('i: ' + str(i))
    # print('j: ' + str(j))
    # for i, r in enumerate(requests):
    #     print(i, r.timestamp)

pp.pprint('Busiest intervals:')
pp.pprint(lib.find_busiest_interval(requests, time_interval = 5, n= 3))
