#!/usr/bin/env python
# encoding: utf-8

import webapp2
import settings
from google.appengine.ext.webapp.util import run_wsgi_app


class WSGIApplication(webapp2.WSGIApplication):
    def __init__(self, *args, **kw):
        super(WSGIApplication, self).__init__(*args, **kw)
        self.router.set_dispatcher(self.__class__.custom_dispatcher)

    @staticmethod
    def custom_dispatcher(router, request, response):
        rv = router.default_dispatcher(request, response)
        # json obj dumps
        if isinstance(rv, dict):
            rv = json.dumps(rv)

        if isinstance(rv, basestring):
            return webapp2.Response(rv)

        return rv

    def route(self, *args, **kw):
        def _wrapper(func):
            self.router.add(webapp2.Route(handler=func, *args, **kw))
            return func
        return _wrapper


app = WSGIApplication(debug=settings.DEBUG)

import views.api_json
import views.api_html
import views.handlers



if __name__ == '__main__':
    run_wsgi_app(app)
