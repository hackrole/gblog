#!/usr/bin/env python
# encoding: utf-8

from os import path
import sys
sys.path.insert(0,
    path.join(path.dirname(path.dirname(path.realpath(__file__))), "google_appengine"
))
print sys.path

import unittest
import webapp2
import blog # the blog apps
from models import Tag, Blog, Category
from google.appengine.ext import testbed


class IndexTest(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

        tag1 = Tag(title='emacs')
        tag2 = Tag(title='vim')
        tag1.put()
        tag2.put()
        cate = Category(title='emacs笔记')
        cate.put()
        b1 = Blog(title="the first emacs blog", text="hello, world",
                  category=cate.key, tags=[tag1.key, tag2.key])
        b2 = Blog(title="the second emacs blog", text="hello, world",
                  category=cate.key, tags=[tag1.key, tag2.key])
        b3 = Blog(title="the third emacs blog", text="hello, world",
                  category=cate.key, tags=[tag1.key, tag2.key])
        b1.put()
        b2.put()
        b3.put()

    def test_index_normal(self):
        request = webapp2.Request.blank('/')
        response = request.get_response(blog.app)
        self.assertEqual(response.status_int, 200)
        self.assertIn('the first emacs blog', response.body)
        self.assertIn('the second emacs blog', response.body)
        self.assertIn('the third emacs blog', response.body)
        # tags
        self.assertIn('emacs', response.body)

if __name__ == '__main__':
    unittest.main()
