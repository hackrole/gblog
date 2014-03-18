#!/usr/bin/env python
# encoding: utf-8


import webapp2
import blog # the blog apps
from models import Tag, Blog, Category
from google.appengine.ext import testbed
from base import BaseTestCase


class IndexTest(BaseTestCase):
    def init_data(self):
        tag1 = Tag(title='emacs')
        tag2 = Tag(title='vim')
        tag1.put()
        tag2.put()
        cate = Category(title='emacs笔记')
        cate.put()
        b1 = Blog(title="the first emacs blog", context="hello, world",
                  category=cate.key, tags=[tag1.key, tag2.key])
        b2 = Blog(title="the second emacs blog", context="hello, world",
                  category=cate.key, tags=[tag1.key, tag2.key])
        b3 = Blog(title="the third emacs blog", context="hello, world",
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


