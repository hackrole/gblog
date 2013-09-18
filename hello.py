#!/usr/bin/env python
# encoding: utf-8

import webapp2
from models import Blog, Tags, Category
from google.appengine.api import users
from webapp2_extras import jinja2
from google.appengine.ext.webapp.util import run_wsgi_app


class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)


class MainPage(BaseHandler):

    def get(self):
        self.render_response("hello.html")

class BnewPage(BaseHandler):
    def get(self):
        t1 = Tags(title="vim")
        t1.put()
        t2 = Tags(title="emacs")
        t2.put()
        c1 = Category(title="vim")
        c1.put()
        blog = Blog(title="just test for fun",
                text="", category=c1.key, tags=[t1.key, t2.key])
        blog.put()
        self.response.write('new blog finish')

class BlistPage(BaseHandler):
    def get(self):
        blogs = Blog.query()
        self.render_response('bl.html', **{'blogs': blogs})


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/bn', BnewPage),
    ('/nl', BlistPage),
], debug=True)


if __name__ == '__main__':
    run_wsgi_app(app)
