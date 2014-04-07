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


DEBUG = True
app = WSGIApplication(debug=DEBUG)


@app.route('/api/blog/get/<blog_str:\w+>')
def blog_get_api(request, blog_str):
    blog_key = ndb.Key(urlsafe=blog_str)
    blog = blog_key.get()
    return blog.to_json_str()


@app.route('/api/blog/list', name='blog_list_api')
def blog_list_api(request):
    pass


@app.route('/api/delete/<model>/<model_str:\w+>', name='model_delete')
def blog_delete_api(request, model, model_str):
    blog_id = ndb.Key(urlsafe=blog_str)
    blog = blog_id.get()
    blog.delete()
    return {'success': True, 'msg': 'ok'}


@app.route('/api/blog/new', name="blog_new")
def blog_new_api(request):
    blog = Blog()
    blog.title = request.POST.get('title')
    blog.content = request.POST.get('content')
    blog.author = request.POST.get('author')
    blog.category = ndb.Key(urlsafe=request.POST.get('category_str'))
    blog.tags = [ndb.Key(urlsafe=tag_str)
            for tag_str in request.POST.get('tags_str').split(',')]
    blog.put()
    return {'blog_str': blog.key.urlsafe()}


@app.route('/api/blog/update/<blog_str:\w+>',
           name='blog_update_api')
def blog_update_api(request, blog_str):
    blog_id = ndb.Key(urlsafe=blog_str)
    blog = blog_id.get()
    blog.title = request.POST.get('title', blog.title)
    blog.content = request.POST.get('content', blog.content)
    blog.author = request.POST.get('author', blog.author)
    blog.category = ndb.Key(urlsafe=request.POST.get('category_str'))
    blog.tags = [ndb.Key(urlsafe=tag_str)
            for tag_str in request.POST.getall('tags_str')]
    blog.put()
    return {'success': True, 'msg': 'ok'}


@app.route("/hello")
def hello(request):
    return "hello world"

# the views handlers
@app.route('/blog/index')
def index(request):
    pass


if __name__ == '__main__':
    run_wsgi_app(app)
