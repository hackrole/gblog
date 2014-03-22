#!/usr/bin/env python
# encoding: utf-8

import webapp2
import sys
import blog
from models import Tag, Blog, Category
from google.appengine.ext import testbed
from base import BaseTestCase


class ModelTest(BaseTestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

        tag1 = Tag(title='emacs')
        tag1.put()
        cate = Category(title='emacs笔记')
        cate.put()
        b1 = Blog(title="the first emacs blog", content="hello, world",
                  category=cate.key, tags=[tag1.key])
        b1.put()

    def tearDown(self):
        pass

    def test_to_json_is_correct(self):
        from models import Tag, Blog, Category
        b = Blog.query().fetch(1)
        print b[0]
        print b[0].to_json()


