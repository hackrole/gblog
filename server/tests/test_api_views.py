#!/usr/bin/env python
# encoding: utf-8

import models
import webapp2
import json
from blog import app as mainapp
from tests.base import BaseTestCase
from google.appengine.ext import testbed
from google.appengine.ext import ndb


class BlogAPITestCase(BaseTestCase):

    def test_blog_get_api(self):
        c = models.Category(title="emacs")
        c.put()
        blog = models.Blog(title="emacs test",
                           content="the first test blog",
                           category=c.key)
        blog.put()
        url = '/api/blog/get/%s' % blog.key.urlsafe()
        request = webapp2.Request.blank(url)
        response = request.get_response(mainapp)

        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.body, blog.to_json_str())

    def test_blog_new_api(self):
        c = models.Category(title="emacs")
        c.put()
        t1 = models.Tag(title="vim")
        t2 = models.Tag(title="emacs")
        t1.put()
        t2.put()
        url = '/api/blog/new'
        post_data = {
            'title': 'vim',
            'content': 'first vim test blog',
            'author': 'hackrole',
            'category_str': c.key.urlsafe(),
            'tags_str': ','.join([t1.key.urlsafe(), t2.key.urlsafe()]),
        }
        request = webapp2.Request.blank(url, POST=post_data)
        request.method = 'POST'
        response = request.get_response(mainapp)

        self.assertTrue(response.status_int, 200)
        blog = models.Blog.query().get()
        self.assertEquals('vim', blog.title)
        self.assertEquals('first vim test blog', blog.content)
