#!/usr/bin/env python
# encoding: utf-8

import webapp2
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


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


if __name__ == '__main__':
    run_wsgi_app(app)
