#!/usr/bin/env python
# encoding: utf-8

"""
base class for unittest.
init testbed for GAE,
and add some data-init tools
"""

import unittest

from google.appengine.ext import testbed


class BaseTestCase(unittest.TestCase):
    """
    base class for GAE app unittest.
    """

    def setUp(self):
        """
        init GAE testbed for unittest
        write data init fun in the sub class to
        load data for test.
        """
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        if hasattr(self, "init_data") and callable(self.init_data):
            self.init_data()

    def testDown(self):
        """
        close GAE testbed, and tear down test data
        write you clean_data fun in sub class to
        tear down data.
        """
        self.testbed.deactivate()
        if hasattr(self, "clean_data") and callable(self.clean_data):
            self.clean_data()
