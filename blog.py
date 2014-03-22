#!/usr/bin/env python
# encoding: utf-8

import webapp2
import json
from lib import markdown
from models import Blog, Tag, Category
from google.appengine.api import users
from webapp2_extras import jinja2
from google.appengine.ext import ndb
from google.appengine.ext.webapp.util import run_wsgi_app


class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render(self, template, **context):
        rv = self.jinja2.render_template(template, **context)
        self.response.write(rv)


class BlogHandler(BaseHandler):
    """
    handlers for the blog interfaces.
    """
    def get(self, blog_id_str):
        """
        get the blog by id
        """
        blog = ndb.Key(urlsafe=blog_id_str).get()

        result = blog.to_json()
        self.response.write(result)

    def list(self):
        """
        get the blog list by condition:w
        """
        page = self.request.get('page', 1)
        page_size = self.request.get('pageSize', 5)
        offset = (page - 1) * page_size
        blog_list = Blog.query().fetch_page(page_size, offset=offset)
        print blog_list
        result = [blog.to_json for blog in blog_list]
        self.response.write(','.join(result))

    def post(self):
        """
        update the blog by id, auth needed
        """
        pass

    def delete(self):
        """
        delete the blog by set status, auth needed
        """
        pass

    def put(self):
        """
        new blog, auth needed
        """

    def put_by_makedown(self):
        """
        put new blog by markupdown file
        """
        pass


class TagHandler(BaseHandler):
    """
    handlers for blog tag
    """

    def get(self):
        """
        get tag by id
        """
        pass

    def list(self):
        """
        get tag list by condition
        """
        pass


class CategoryHandler(BaseHandler):
    """
    handlers for blog category
    """
    def get(self):
        """
        get category by id
        """
        pass

    def list(self):
        """
        get category list by condition
        """
        pass


urls = [
    ('/blog/get/(\w+)', BlogHandler),
    webapp2.Route('/blog/list', handler='blog.BlogHandler:list', name="blog/list")
]

app = webapp2.WSGIApplication(
    urls,
    debug=True
)


if __name__ == '__main__':
    run_wsgi_app(app)
