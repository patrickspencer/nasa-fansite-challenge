# -*- coding: utf-8 -*-

"""
models.py
~~~~~~~~~
Part of the Nasa Fansite Anaslytics Challenge, an Insight Data Engineer
programming challenge.

models.py: contains the main models for the program

:copyright: (c) 2017 by Patrick Spencer.
"""

import re
from datetime import datetime


class Request(object):
    def __init__(self, request_str):
        """Regex line
        :param request_str: a string of the form
            '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] \
                "GET /blah.jpg HTTP/1.0" 200 345'
        :return: tuple of request attrributes that looks like:
            ('199.72.81.55', '01/Jul/1995:00:00:01 -0400', 'GET', '/blah.jpg HTTP/1.0', '200', '345')
                Notice
        """

        """Explanation of regex
        :param request_str: a string of the form
            '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] \
            "GET /blah.jpg HTTP/1.0" 200 345'
        :return: tuple of request attrributes that looks like:
            ('199.72.81.55', '01/Jul/1995:00:00:01 -0400', 'GET /blah.jpg HTTP/1.0', '200', '345')
        Notice '/blah.jpg HTTP/1.0' doesn't separate resource and protocol so
        we do that later with split()
        """
        # regex = '(.*)\"(.*)\"(.*)\s(\S*|-)(?:\n)'
        # regex = '(.*)\"(.*)\"(.*)\s(\S*|-)(?:\n)'
        # ('199.72.81.55', '01/Jul/1995:00:00:01 -0400', 'GET', '/blah.jpg HTTP/1.0', '200', '345')
        regex = '(.*?) - - \[(.*?)\] "(.*)" (\d\d\d)\s(.+)'
        try:
            groups = re.match(regex, request_str).groups()
        except AttributeError:
            False

        dt = datetime.strptime(groups[1], '%d/%b/%Y:%H:%M:%S %z')
        resource = groups[3].split(' ')
        # check if bytes is set to - which happens on 302 or 404 responses
        if groups[-1] == '-':
            self.bytes = 0
        else:
            self.bytes = int(groups[-1])

        if groups:
            host_str_arr = groups[2].split(' ')
            # groups looks like one of the three options:
            # 1. GET /blah.jpg HTTP/1.0
            # 2. GET /blah.jpg
            # 3. blah
            method = ''
            protocol = ''
            resource = ''
            if len(host_str_arr) == 1:
                resource = host_str_arr[0]
            if len(host_str_arr) == 2:
                method = host_str_arr[0]
                resource = host_str_arr[1]
            if len(host_str_arr) == 3:
                method = host_str_arr[0]
                resource = host_str_arr[1]
                protocol = host_str_arr[2]

        self.request_str = request_str.rstrip()
        self.groups = groups
        self.host = groups[0]
        self.date_str = groups[1]
        self.date = dt
        self.timestamp = int(dt.timestamp())
        self.method = method
        self.resource = resource
        self.protocol = protocol
        self.response = groups[3]
