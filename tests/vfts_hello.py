#!/usr/bin/env python
# encoding: utf-8

import webapp2
import json
from main import app as mainapp
from tests.base import BaseTestCase
from google.appengine.ext import testbed
from google.appengine.ext import ndb


class VFTSHelloTestCase(BaseTestCase):
    BASE_URL = "http://localhost:8080"

    def setUp(self):
        super(VFTSHelloTestCase, self).setUp()
        self.webbrowser = FireFox()

    def test_hello_always_return_same_string(self):
        url = '/'.join([BASE_URL, '/hello'])

        self.webbrowser.get(url)

        self.assertEqual('hello world', self.webbrowser.body)
