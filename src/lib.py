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
                bad_logins.append(r.request_str)
            else:
                update_401_d(d, r, block_list)
    return bad_logins

def write_blocked(failed_logins):
    """Write the entries a failed login array (which is an array of request
    strings that record when failed logins happend) to the file blocked.txt

    :param failed_logins: an array of login attempts within a 5 minute ban
        windows. The array would look like this:

    ['207.109.29.70 - - [01/Jul/1995:01:28:41 -0400] "POST /login HTTP/1.0" 401 1420',
     '207.109.29.70 - - [01/Jul/1995:01:35:14 -0400] "POST /login HTTP/1.0" 401 1420',
     '207.246.17.94 - - [01/Jul/1995:02:51:27 -0400] "POST /login HTTP/1.0" 401 1420']

    :return: Null
    """
    file_name = 'blocked.txt'
    output_location = settings.log_output_file(file_name)
    try:
        os.remove(output_location)
    except OSError:
        pass
    with open(output_location, 'a') as file:
        for line in failed_logins:
            file.write(line + '\n')

def update_top_dict(d, key, value, n = 10):
    """Update the dict holding the top values. Checks to see if
    value is greater than the minimum value of d. Also deletes
    smallest value of d if d has more than n elements

    :param d: the dict holding the top values. It's of the form:
        d = {'a': 10,
             'b': 4,
             'c': 2,
             'd': 8}

    :param key: the name of the value to check the dict against
    :param value: the value to check to see is in the top n elements
    :param n: how many elements the dict d should have
    :return: an updated dict d.
    """
    if value > min_value(d):
        d[key] = value
        if len(d) > n:
            d.pop(min_key(d), None)
    return d

def find_busiest_interval(requests, time_interval, n=10):
    """Find the n top time intervals with the most requests in them. We
    can view requests as a sequence of non-decreasing sequence of
    integers (unixtime stamps). This function searches to find what the
    busiest block of time is. The length of the block of time id td
    (time delta) in seconds.

    :param requests: a list of :class:`Request ,
    :param time_interval: the length of the time intervals
    :param n: The dict will return the top n intervals with the most
        requests
    :return: a dist of the form
        {804571209: 20,
         804571210: 21,
         804571211: 24}
        where somethign like 804571209 is the unix time stamp of the
        start of the interval which has 20 requests in it.
    """

    def t(i):
        """The timestamp of the ith request"""
        return requests[i].timestamp

    # The interval length in seconds
    top_n = {}
    top_n['null'] = 0
    a = requests[0].timestamp
    max_time = requests[-1].timestamp
    i, j = 0, 0
    while a+time_interval <= max_time+1:
        # delete times that shouldn't be in bin
        # print(' --- --- --- ---')
        # print('Time interval: [' + str(a) + ',' + str(a+time_interval - 1) + ']')
        # print('starting i: ' + str(i))
        # print('starting j: ' + str(j))
        while t(i) < a:
            i += 1
        # Find the the smallest j value so that t(j) < a + time_delta
        while t(j+1) < a + time_interval:
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
        # m = number of elements in the interval
        if j+1 == len(requests)-1:
            # this whole algorithm doesn't count the last item in the last interval
            m = j - i + 2
        else:
            m = j - i + 1
        # print('number of elements in time interval: ' + str(m) )
        # print('i: ' + str(i))
        # print('t(i): ' + str(t(i)))
        # print('requests[i].host: ' + str(requests[i].host))
        update_top_dict(top_n, a, m, n)
        # print('m: ' + str(m))
        # print(top_ten)
        a = a + 1
    return top_n
