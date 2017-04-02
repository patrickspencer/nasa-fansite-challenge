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

import lib
import settings

if __name__ == "__main__":
    start_time = time.time()

    log_file = settings.load_log_file('log_head.txt')
    requests = lib.read_file(log_file)
    # hosts = create_freq_hash(requests, n=-1, m=0)
    # write_file(top_freq(hosts),'hosts.txt')

    pp = pprint.PrettyPrinter(indent=4)


    for request in requests:
        print(request)
        r = models.Request(request)

    print("--- %s seconds ---" % (time.time() - start_time))
