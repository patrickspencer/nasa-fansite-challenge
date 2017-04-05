# -*- coding: utf-8 -*-

"""
lib.py
~~~~~~
Part of the Nasa Fansite Anaslytics Challenge, an Insight Data Engineer
programming challenge.

lib.py contains helper functions

:copyright: (c) 2017 by Patrick Spencer.
:license: Don't touch my stuff. But seriously, a restrictive EULA. See LICENSE
    for more details.
"""

import re
import os
import models
import settings

def read_file(log_file):
    """Read main log file and return of list of lines

    :param log_file: ascii log file
    :return: :class:`Request <Request>`: object
    :rtype: models.Request
    """
    requests = []
    # TODO: fix error handling of open command. Right now we set it to ignore
    #       incase something goes wrong
    with open(log_file, 'r', encoding='us-ascii', errors='ignore') as file_lines:
        for line in file_lines:
            requests.append(models.Request(line))
            # requests.append(line)
    return requests

def update_hash_freq(d, key):
    """Look for key in d. If key exists add one to frequency count. If it
    doesn't exist, add the key and set frequency to 1

    :param d: dict
    :param key: string name of key
    :return: void
    """
    d[key] = d.get(key, 0) + 1

def create_host_freq_hash(requests):
    """Creates frequency hash.

    :param l: list of :class:`Request <Request>` objects
    :param n: first n elements of the list l to create a frequency hash table
        from. Used for testing purposes because sometimes the list l is just too
        darn big to go through the whole thing.
    :return: frequency dict
    :rtype: dict
    """
    d = {}
    for r in requests:
        update_hash_freq(d, r.host)
    return d

def min_key(d):
    """Search through a dict and get the key with the minimum value.

    :param d: dict where the values are postive integers
        {'a': 0, 'b': 4, 'c': 2}
    :return: key value of entry with smallest value
    :rtype: string

    Usage::

        >>> d = {'a': 10,
                 'b': 4,
                 'c': 2,
                 'd': 8,
                 'e': 7,
                 'f': 5}
        >>> min_key(d)
        'c'
    """
    return min(d, key=d.get)

def min_value(d):
    """Search through a dict and get the minimum value.

    :param d: dict where the values are postive integers
        {'a': 0, 'b': 4, 'c': 2}
    :return: value of entry with smallest value
    :rtype: int

    Usage::

        >>> d = {'a': 10,
                 'b': 4,
                 'c': 2,
                 'd': 8,
                 'e': 7,
                 'f': 5}
        >>> min_key(d)
        2
    """
    return d[min_key(d)]

def max_key(d):
    """Search through a dict and get the key with the max value.

    :param d: dict where the values are postive integers
        {'a': 0, 'b': 4, 'c': 2}
    :return: key value of entry with smallest value
    :rtype: string

    Usage::

        >>> d = {'a': 10,
                 'b': 4,
                 'c': 2,
                 'd': 8,
                 'e': 7,
                 'f': 5}
        >>> max_key(d)
        'a'
    """
    return max(d, key=d.get)

def max_value(d):
    """Search through a dict and get the minimum value.

    :param d: dict where the values are postive integers
        {'a': 0, 'b': 4, 'c': 2}
    :return: key value of entry with smallest value
    :rtype: integer

    Usage::

        >>> d = {'a': 10,
                 'b': 4,
                 'c': 2,
                 'd': 8,
                 'e': 7,
                 'f': 5}
        >>> min_value(d)
        '2'
    """
    return d[max_key(d)]

def top_freq(d, n=10):
    """Create a min hash of the entries in d with the top n frequencies
    :param d: dict where the values are postive integers
        {'a': 0, 'b': 4, 'c': 2}
    :param n: the n keys with the highest value. Defaults to 10.
    :return: subdict of d with n entries
    :rtype: dict
    """
    # top is a min heap of most frequent domains of d
    top = {}
    top["null"] = 0
    for index, key in enumerate(d):
        # The top frequencies don't take into account if there
        # are multiple ips with the same frequency.
        # TODO: figure out what to do about ips with the same frequencies
        if d[key] > min_value(top):
            top[key] = d[key]
            if len(top) > n:
                top.pop(min_key(top), None)
    return top

def order_dict(d):
    """Order the elements of a dict by their values and return a list

    :param d: dict where the values are postive integers
        {'a': 0, 'b': 4, 'c': 2}
    :param: destination file name "ex: hosts.txt"
    :return: list of tuples the type:
    [('b',4), ('c',2), ('a',)]
    """

def write_file(d, file_name, include_values=True):
    """Write the entries of a dict to a file.

    :param d: dict where the values are postive integers
        {'a': 0, 'b': 4, 'c': 2}
    :param file_name: destination file name "ex: hosts.txt". Each line of the
        destination file looks like `key,value` and the lines are ordered in
        descending order by the value of the dicts. For example, with the above
        example input file, the output file might look like this :
        b,4
        c,2
        a,0
    :param include_values: Bool: whether or not to include a comma and then
        values of dict entries. For examples:

            >>> write_file({'a': 0, 'b': 4, 'c': 2}, file, True)
            b,4
            c,2
            a,0
            >>> write_file({'a': 0, 'b': 4, 'c': 2}, file, False)
            b
            c
            a

    :return: Null
    """
    output_location = settings.log_output_file(file_name)
    try:
        os.remove(output_location)
    except OSError:
        pass
    with open(output_location, 'a') as file:
        while d:
            max_key(d)
            if include_values:
                file.write(max_key(d) + "," + str(max_value(d)) + "\n")
            else:
                file.write(max_key(d) + "\n")
            d.pop(max_key(d), None)

def create_bytes_dict(file):
    """Reads file line by line makesdict that has entries like

    :param file: full file name to load
    :return: something that looks like this
        {
        'resource1': bytes_used,
        'resource': bytes_used,
        }
    """
    d = {}
    with open(file, 'r', encoding='us-ascii', errors='ignore') as file_lines:
        for i, line in enumerate(file_lines):
            r = models.Request(line)
            # print('Line: ' + str(i))
            d[r.resource] = d.get(r.resource, 0) + r.bytes
    return d

def get_top_dict_values(d, n=10):
    """Return a dict of entries of the dict d which have the top n values

    :param file: dict that looks like this
        {
        'key1': value1,
        'key2': value1,
         etc...
        }
    :return: dict of top n values
        {
        'key1': value1,
        'key2': value1,
        }
    """

    top = {}
    for i in range(0,n):
        key = max_key(d)
        value = max_value(d)
        top[key] = value
        del d[key]
    return top

def remove_min(arr):
    """Remove the minimum value from an array
    :param arr: array
    :rtype: list
    """
    return arr.remove(min(arr))

def update_block_list(d, host, timestamp):
    """add a host to the block list
    :param d: dict of the form:
        {
            'host1': [804612566, 804612567, 804612568]
        }
    :param host: host
    :param timestamp: the unix timestamp of the last timestamp of the 3
        consecutive failed logins within a certain 20 sec period
    """
    if host not in d:
        d[host] = [timestamp]
    else:
        d[host].append(timestamp)
    return d

def update_401_d(d, r, block_list):
    """Updates dict that assigns a host to an array of unix timestamps for 401 access errors for that host
    :param d: dict
    :param r: :class:`Request <request>`
    :param block_list: a ban_list dict that keeps track of which hosts have been blocked
    :return: a dict of this form:
    {
    'host1': [804612566, 804612567, 804612568]
    'host2': [804626197, 804626198]
    }
    All timestamp arrays have at most 3 time stamps since we only need to compare the last 3 logins
    """
    if r.host not in d:
        d[r.host] = [r.timestamp]
    else:
        # for failed_login_time in d[r.host]:
            # if r.date - failed_login_time
        # we prune the array down to 2 before we add the current request
        # since we only need to compare the current request timestamp to
        # the last 2
        last_logins = d[r.host]
        if len(last_logins) >= 3:
            remove_min(d[r.host])
        last_logins.append(r.timestamp)
        # we now have an array (d[r.host]) with 3 time stamps
        # We only need to find the difference between the max and min
        # because if this difference is 20 secs or greater than so is the
        # difference between the max and middle or the middle and min.
        if len(last_logins) ==3 and max(last_logins) - min(last_logins) <= 20:
            update_block_list(block_list, r.host, max(last_logins))

def check_for_mult_logins(requests):
    """Check a list of requests to see if there are 3 or more 401 request
    responses within a 20 second period
    :param requests: :class:`Request <request>`
    :return: a ditionary or blocked hosts that looks like
    """
    # d is the dictionary that temporarily holds the last 3 login attempts
    d = {}
    # block_list is the dictionary that holds when a host was blocked
    block_list = {}
    # bad_logins is an array that holds logins after a ban was started but
    # before the 5 minute ban period has ended
    bad_logins = []
    for r in requests:
        if r.response == '401':
            if r.host in block_list and r.timestamp - max(block_list[r.host]) <= 300:
                bad_logins.append([r.host, r.date_str])
            else:
                update_401_d(d, r, block_list)
    return bad_logins
