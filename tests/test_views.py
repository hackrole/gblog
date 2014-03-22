#!/usr/bin/env python
# encoding: utf-8


import webapp2
import json

import blog # the blog apps
from models import Tag, Blog, Category
from google.appengine.ext import testbed
from base import BaseTestCase


class BlogTest(BaseTestCase):

    def init_data(self):
        pass

    def test_getblog_by_id(self):
        t1 = Tag(title='emacs')
        t2 = Tag(title='vim')
        t1.put()
        t2.put()
        c1 = Category(title='emacs笔记')
        c1.put()
        b = Blog(title="the first emacs blog", content="hello, world",
                  category=c1.key, tags=[t1.key, t2.key])
        b.put()

        url = "/blog/get/%s" % b.key.urlsafe()
        request = webapp2.Request.blank(url)
        response = request.get_response(blog.app)
        blog_obj = json.loads(response.text)

        self.assertEqual(response.status_int, 200)
        self.assertEqual(blog_obj['id'], b.key.urlsafe())
        self.assertEqual(blog_obj['title'], b.title)
        self.assertEqual(blog_obj['content'], b.content)
        self.assertEqual(blog_obj['create_time'],
                         b.create_time.strftime('%Y-%m-%d %H:%M:%s'))
        self.assertEqual(blog_obj['update_time'],
                         b.update_time.strftime('%Y-%m-%d %H:%M:%s'))
        self.assertEqual(blog_obj['category_id'], c1.key.urlsafe())
        self.assertEqual(blog_obj['tags_id'],
                         [t1.key.urlsafe(), t2.key.urlsafe()])

    def test_blog_list(self):
        t1 = Tag(title='emacs')
        t2 = Tag(title='vim')
        t1.put()
        t2.put()
        c1 = Category(title='emacs笔记')
        c1.put()
        b1 = Blog(title="the first emacs blog", content="hello, world",
                  category=c1.key, tags=[t1.key, t2.key])
        b1.put()
        b2= Blog(title="the second emacs blog", content="hello, world",
                  category=c1.key, tags=[t1.key, t2.key])
        b2.put()

        url = "/blog/list?pageSize=10"
        request = webapp2.Request.blank(url)
        response = request.get_response(blog.app)
        print '>>>>>>>>>>>>>'
        print response.text
        blog_obj = json.loads(response.text)

        self.assertEqual(response.status_int, 200)
        self.assertEqual(len(blog_obj), 2)
