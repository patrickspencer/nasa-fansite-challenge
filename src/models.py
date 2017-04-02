# -*- coding: utf-8 -*-

"""
models.py
~~~~~~~~~
Part of the Nasa Fansite Anaslytics Challenge, an Insight Data Engineer
programming challenge.

models.py: contains the main models for the program

:copyright: (c) 2017 by Patrick Spencer.
:license: Don't touch my stuff. But seriously, a restrictive EULA. See LICENSE
    for more details.
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
            ('199.72.81.55', '01/Jul/1995:00:00:01 -0400', 'GET', '/blah.jpg HTTP/1.0', '200', '345')
        Notice '/blah.jpg HTTP/1.0' doesn't separate resource and protocol so
        we do that later with split()
        """
        regex = '(.*?) - - \[(.*?)\] "(\w*?)\s(.*?)" (\d\d\d)\s(.+)'
        try:
            groups = re.match(regex, request_str).groups()
        except AttributeError:
            False

        datetime_object = datetime.strptime(groups[1], '%d/%b/%Y:%H:%M:%S %z')
        resource = groups[3].split(' ')
        # check if bytes is set to - which happens on 302 or 404 responses
        if groups[5] == '-':
            self.bytes = 0
        else:
            self.bytes = int(groups[5])

        self.groups = groups
        self.host = groups[0]
        self.date_str = groups[1]
        self.date = datetime_object
        self.method = groups[2]
        self.resource = resource[0]
        if len(resource) > 1:
            self.protocol = resource[1]
        else:
            self.protocol = None
        self.response = groups[4]
