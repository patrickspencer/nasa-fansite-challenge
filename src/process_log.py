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

def update_hash(d, key):
    """Look for key in d. If key exists add one to frequency count. If it doesn't
    exist, add the key and set frequency to 1

    :param d: dict
    :param d: string name of key
    :return: void
    """
    d[key] = d.get(key, 0) + 1

def create_freq_hash(l, n=-1):
    """Creates frequency hash.

    :param l: list or tuples of the form
        ('199.72.81.55', '01/Jul/1995:00:00:01 -0400', 'GET', '/', 'HTTP/1.0', '200', '345')
    :param n: first n elements of the list l to create a frequency hash table
        from. Used for testing purposes because sometimes the list l is just too
        darn big.
    :return: frequency dict
    :rtype: dict
    """
    d = {}
    for request in l[0:n]:
        update_hash(d, parse_request(request)[0])
    return d

def create_freq_hash(l, n=-1):
    """Creates frequency hash.

    :param l: list or tuples of the form
        ('199.72.81.55', '01/Jul/1995:00:00:01 -0400', 'GET', '/', 'HTTP/1.0', '200', '345')
    :param n: first n elements of the list l to create a frequency hash table
        from. Used for testing purposes because sometimes the list l is just too
        darn big.
    :return: frequency dict
    :rtype: dict
    """
    d = {}
    for request in l[0:n]:
        update_hash(d, parse_request(request)[0])
    return d

def min_key(d):
    """Search through a dict and get the key with the minimum value.

    :param d: dict where the values are postive integers
        {'a': 0, 'b': 4, 'c': 2}
    :return: key value of entry with smallest value
    :rtype: string
    """
    return min(d, key=d.get)

def min_value(d):
    """Search through a dict and get the minimum value.

    :param d: dict where the values are postive integers
        {'a': 0, 'b': 4, 'c': 2}
    :return: key value of entry with smallest value
    :rtype: integer
    """
    return d[min_key(d)]

if __name__ == "__main__":
    start_time = time.time()

    log_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = os.path.join(log_file_dir, 'log_input', 'log_head.txt')

    requests = read_file(log_file)
    d = create_freq_hash(requests, n=100)
    # top is a min heap of most frequent ips of
    top = {}
    top["null"] = 0
    for value, key in enumerate(d):
        # the > isn't a >= so the top frequencies don't take into account if there
        # are multiple ips with the same frequency.
        # TODO: figure out what to do about ips with the same frequencies
        if int(value) > min_value(top):
            top[key] = value
            if len(top) >= 10:
                top.pop(min_key(top), None)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(top)

    print("--- %s seconds ---" % (time.time() - start_time))
