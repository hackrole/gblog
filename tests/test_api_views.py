#!/usr/bin/env python
# encoding: utf-8

import models
import webapp2
import webtest
from .base import BaseTestCase
from google.appengine.ext import testbed
from google.appengine.ext import ndb


class BlogAPITestCase(BaseTestCase):

    def test_blog_get(self):
        c = models.Category(title="emacs")
        c.put()
        blog = models.Blog(title="emacs test",
                           content="the first test blog",
                           category=c.key)
        blog.put()




