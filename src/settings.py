# -*- coding: utf-8 -*-

"""
settings.py
~~~~~~~~~~~~~~
Part of the Nasa Fansite Analytics Challenge, an Insight data Engineer
programming challenge.

settings.py contains file paths and other settings

:copyright: (c) 2017 by Patrick Spencer.
"""

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_input_dir = os.path.join(base_dir, 'log_input')
log_output_dir = os.path.join(base_dir, 'log_output')
fixture_dir = os.path.join(base_dir, 'insight_testsuite', 'local', 'fixtures')

def load_log_file(file_name):
    return os.path.join(log_input_dir, file_name)

def load_fixture(file_name):
    return os.path.join(fixture_dir, file_name)

def log_output_file(file_name):
    return os.path.join(log_output_dir, file_name)

