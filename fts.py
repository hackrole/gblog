#!/usr/bin/env python
# encoding: utf-8

import unittest
import time
from selenium import webdriver
from models import Tag, Category, Blog


def testdb_init():
    # db clear
    Blog.all().delete()
    Tag.all().delete()
    Category.all().delete()

    t1 = Tag(title="emacs")
    t2 = Tag(title="python")
    t1.put()
    t2.put()

    c1 = Category(title='program')
    c2 = Category(title='edit')
    c1.put()
    c2.put()

    b1 = Blog(title='first blog')
    b1.context = "this is my first blog, hello world"
    b1.put()
    b2 = Blog(title="second blog")
    b2.context = "this is my second blog, hello python"
    b2.tags = [t1, t2]
    b2.put()
    b3 = Blog(title="third blog")
    b3.context = "this is my third blog, hello python"
    b3.tags = [t1,]
    b3.tags = c2
    b3.put()
    b4 = Blog(title="fourth blog")
    b4.context = "this is my fourth blog, hello python"
    b4.tags = [t2,]
    b4.category = c1
    b4.put()


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.ff = webdriver.Firefox()
        self.base_url = "localhost:8080"
        self.ff.implicitly_wait(3)

    def tearDown(self):
        self.ff.quit()


class BlogIndexTestCase(BaseTestCase):
    def setUp(self):
        super(BlogIndexTestCase, self).setUp()
        # TODO: data init
        testdb_init()

    def test_blog_index_page(self):
        url = self.base_url
        self.ff.get(url)
        time.sleep(10)



if __name__ == '__main__':
    unittest.main()
