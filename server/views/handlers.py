#!/usr/bin/env python
# encoding: utf-8

import webapp2
import json
import settings
from main import app
from utils import admin_auth, render_template
from models import Blog, Tag, Admin
from google.appengine.api import users
from google.appengine.ext import ndb


@app.route("/hello")
def hello(request):
    admin_auth(request)
    admin = Admin.query().get()
    return "hello world, %s" % admin.name


@app.route('/index')
def index(request):
    blog_list = Blog.query().fetch()
    return render_template('index.html', blog_list=blog_list)


@app.route('/detail/<blog_str:.+>')
def detail(request, blog_str):
    blog = Blog.get_by_urlsafe(blog_str)
    return render_template('detail.html', blog=blog)
