#!/usr/bin/env python
# encoding: utf-8

import webapp2
import json
import settings
from main import app
from utils import admin_auth
from models import Blog, Tag, Admin
from google.appengine.api import users
from google.appengine.ext import ndb


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


@app.route('/api/blog/get/<blog_str:.+>')
def blog_get_api(request, blog_str):
    blog_key = ndb.Key(urlsafe=blog_str)
    blog = blog_key.get()
    return blog.to_json_str()


@app.route('/api/blog/list', name='blog_list_api')
def blog_list_api(request):
    blog_list = Blog.query().fetch()
    return json.dumps([blog.to_json() for blog in blog_list])


@app.route('/api/blog/delte/<blog_str:.+>', name='blog_delete_api')
def blog_delete_api(request, blog_str):
    blog = Blog.get_by_urlsafe(blog_str)
    blog.delete()
    return {'success': True, 'msg': 'ok'}


@app.route('/api/blog/new', name="blog_new_api")
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


@app.route('/api/tag/new', name='tag_new_api')
def tag_new_api(request):
    if not admin_auth(request):
        webapp2.abort(500)
    tag = Tag()
    tag.title = request.POST.get('title')
    tag.put()
    return {'success': True, 'msg': 'ok'}


@app.route('/api/tag/create', name='create_tags_api')
def tags_create_api(request):
    """ create a list of tags """
    if not admin_auth(request):
        webapp2.abort(500)

    tag_list = request.POST.get('tags_str').splite(':')
    for tag in tag_list:
        tag = Tag()
        tag.title = request.POST.get('title')
        tag.put()
    return {'success': True, 'msg': 'ok'}


@app.route('/api/tag/list', name='tag_list_api')
def tag_list_api(request):
    """ list tag pages """
    page_str = request.GET.get('page_str')
    page_action = request.GET.get('page_action', 'before')
    page_size = int(request.GET.get('page_size', 5))

    q = Tag.query()
    #if page_action == 'before':
        #q = q.filter(Tag.key >= ndb.Key(urlsafe=page_str))
    #elif page_action == 'after':
        #q = q.filter(Tag.key <= ndb.Key(urlsafe=page_str))
    #else:
        #return {'success': False, 'msg': 'page action unknow.'}

    tag_list = q.fetch_page(page_size)

    # TODO: page obj to json
    return json.dumps([tag.to_json() for tag in tag_list])
