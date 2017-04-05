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

if __name__ == "__main__":
    start_time = time.time()

    log_file_name = 'log_head_30.txt'
    log_file = settings.load_log_file(log_file_name)
    requests = lib.read_file(log_file)

    top_ten = {}
    top_ten['null'] = 0
    def update_top_ten(d, key, value, n = 10):
        if value > lib.min_value(d):
            d[key] = value
            if len(d) > n:
                d.pop(lib.min_key(d), None)
    # update_top_ten(top_ten, )


    a = requests[0].timestamp
    # The interval length in seconds
    time_delta = 5
    max_time = requests[-1].timestamp
    def t(i):
        """The timestamp of the ith request"""
        return requests[i].timestamp
    i = 0
    j = 0
    # print(max_time)
    # print('Start time: ' + str(a))
    while a+time_delta <= max_time+1:
        # delete times that shouldn't be in bin
        print(' --- --- --- ---')
        # print('Start another round of a++: i, j: ' + str(i) + ',' + str(j))
        print('Time interval: [' + str(a) + ',' + str(a+time_delta - 1) + ']')
        # print('starting i: ' + str(i))
        # print('starting j: ' + str(j))
        while t(i) < a:
            i += 1
        # Find the the smallest j value so that t(j) < a + time_delta
        while t(j+1) < a + time_delta:
            # print('t(j) inside while loop: ' + str(t(j)))
            # print('j+1 < len(requests): ' + str(j+1 < len(requests)))
            # print('j+1: ' + str(j+1))
            # print('len(requests) ' + str(len(requests)))
            # check to see we haven't reached the end of the array
            if j+1 < len(requests)-1:
                j += 1
            else:
                break
            # print('j inside while loop: ' + str(j))
        # print('a+time_delta: ' + str(a + time_delta))
        # print('i: ' + str(i))
        # print('j: ' + str(j))
        # print('First element in this interval: t(' + str(i) + '): ' + str(t(i)))
        # print('Last element in this interval: t(' + str(j) + '): ' + str(t(j)))
        # print('i: ' + str(i))
        # print('j: ' + str(j))
        # m = number of elements in the interval
        # print(j)
        # print(len(requests))
        if j+1 == len(requests)-1:
            m = j - i + 2
        else:
            m = j - i + 1
        print('number of elements in time interval: ' + str(m) )
        # print('i: ' + str(i))
        # print('t(i): ' + str(t(i)))
        # print('requests[i].host: ' + str(requests[i].host))
        update_top_ten(top_ten, a, m, n = 3)
        print('m: ' + str(m))
        print('requests[i].timestamp: ' + str(requests[i].timestamp))
        print('i: ' + str(i))
        print('lib.min_value(d): ' + str(lib.min_value(top_ten)))
        print('m > lib: min_value(top_ten)' + str(m > lib.min_value(top_ten)))
        print(top_ten)
        a = a + 1
    # print('i: ' + str(i))
    # print('j: ' + str(j))
    # for i, r in enumerate(requests):
    #     print(i, r.timestamp)

