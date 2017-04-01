# -*- coding: utf-8 -*-

"""
go.py
~~~~~
Part of the Nasa Fansite Anaslytics Challenge, an Insight Data Engineer
programming challenge

:copyright: (c) 2017 by Patrick Spencer.
:license: MIT, see LICENSE for more details.
"""

import re
import os
import time

def read_file(log_file):
    """Read main log file

    :param file: ascii log file
    :return: list of strings that look like this:
        '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET / HTTP/1.0" 200 345'
    :rtype: list
    """
    requests = []
    # TODO: fix error handling of open command
    with open(log_file, 'r', encoding='us-ascii', errors='ignore') as file_lines:
        for line in file_lines:
            requests.append(line)
    return requests

def parse_request(request):
    """Regex a request line from log file

    :param request: a string of the form:
        '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET / HTTP/1.0" 200 345'
    :return: list that looks like:
        ['199.72.81.55', '01/Jul/1995:00:00:01 -0400', 'GET', '/', 'HTTP/1.0', '200', '345']
    :rtype: list
    """
    regex = '(.*?) - - \[(.*?)\] "(.*?)" (\d\d\d) (.*?)'
    try :
        return re.match(regex, request).groups()
    except AttributeError:
        return False

def update(d, key):
    """Update hash file. If key exists add one to support count. If it doesn't
    exist, add the key and set support to 1

    :param d: dict
    :param d: string name of key
    :return: void
    """
    d[key] = d.get(key, 0) + 1

if __name__ == "__main__":
    start_time = time.time()

    log_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = os.path.join(log_file_dir, 'log_input', 'log_head.txt')

    requests = read_file(log_file)
    d = {}
    for request in requests:
        r = parse_request(request)
        update(d, r[0])
        # print(r[0])
        # print("request: " + request)
    # print(d)
    # parsed_requests = [parse_request(r) for r in requests]

    print("--- %s seconds ---" % (time.time() - start_time))
