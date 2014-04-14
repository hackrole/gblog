#!/usr/bin/env python
# encoding: utf-8

import webapp2
import json
from lib import markdown
from webapp2_extras import jinja2
from models import Blog, Tag, Admin
from google.appengine.api import users
from webapp2_extras import jinja2
from google.appengine.ext import ndb
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users


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

def render_template(template, **kw):
    render = jinja2.get_jinja2(app=app)
    rv = render.render_template(template, **kw)
    return rv


def admin_auth(request):
    email = request.params.get('email', '')
    pwd = request.params.get('pwd', '')
    if not Admin.auth(email, pwd):
        webapp2.abort(401, "admin required")
    return True


@app.route('/api/admin_init')
def admin_init(request):
    """ init the admin by the browser login """
    if not users.is_current_user_admin():
        result = "<a href='%s'>登录</a>" % users.create_login_url('/api/admin_init')
        return result

    admin = Admin()
    admin.email = "daipeng123456@gmail.com"
    admin.name = "hackrole"
    admin.password = '123456'
    admin.put()
    return "admin init success"


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
    if not admin_auth(request):
        webapp2.abort(500)
    blog = Blog()
    blog.title = request.POST.get('title')
    blog.content = request.POST.get('content')
    blog.put()
    return {'blog_str': blog.key.urlsafe()}


@app.route('/api/blog/update/<blog_str:\w+>',
           name='blog_update_api')
def blog_update_api(request, blog_str):
    blog = Blog.get_by_urlsafe(blog_str)
    blog.title = request.POST.get('title', blog.title)
    blog.content = request.POST.get('content', blog.content)
    blog.put()
    return {'success': True, 'msg': 'ok'}


# modules
@app.route('/module/hot_tags', name='hot_tags_tapi')
def hot_tags_module(request):
    limit = int(request.GET.get('limit'))
    tags = Tags.query().order('-order').fetch(limit)
    return render_template('hot_tags', tags=tags)



@app.route('/module/blog_detail/<blog_str:\w+>', name='detail')
def blog_detail_module(request, blog_str):
    blog = ndb.Key(urlsafe=blog_str).get()
    return render_template('blog_detail', blog=blog)

@app.route('/module/blog_list', name='blog_list')
def blog_list_module(request):

    return render_template('blog_list', blogs=blogs)


@app.route("/hello")
def hello(request):
    admin_auth(request)
    admin = Admin.query().get()
    return "hello world, %s" % admin.name


# the views handlers
@app.route('/index')
def index(request):
    blog_list = Blog.query().fetch()
    hot_tags = Tag.query().fetch()
    print hot_tags
    return render_template('index.html',
                           blog_list=blog_list, hot_tags=hot_tags)

@app.route('/detail/<blog_str:.+>')
def detail(request, blog_str):
    blog = Blog.get_by_urlsafe(blog_str)
    hot_tags = Tag.query().fetch()
    return render_template('detail.html',
                           blog=blog, hot_tags=hot_tags)


if __name__ == '__main__':
    run_wsgi_app(app)
