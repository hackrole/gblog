#!/usr/bin/env python
# encoding: utf-8

import unittest
import time
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.ff = webdriver.Firefox()
        self.base_url = "localhost:8080"
        self.ff.implicitly_wait(3)

    def tearDown(self):
        self.ff.quit()


class StaticTestCase(BaseTestCase):

    def test_can_get_static_html(self):
        base_url = self.base_url + "/static/static_html/"
        # the the static index.html
        self.ff.get(base_url +'index.html')
        blog_title = self.ff.find_element_by_xpath('//h2')
        self.assertEqual(u"hackrole's home", blog_title.text)

    def test_can_get_the_jquery(self):
        pass

class BlogIndexTestCase(BaseTestCase):
    def setUp(self):
        super(BlogIndexTestCase, self).setUp()

    def test_blog_index_page(self):
        url = self.base_url
        self.ff.get(url)
        time.sleep(10)



if __name__ == '__main__':
    unittest.main()
