#!/usr/bin/env python
# encoding: utf-8

import webapp2
import json
import settings
from jinja2 import Environment, FileSystemLoader
from models import Blog, Tag, Admin
from utils import admin_auth
from google.appengine.api import users
from webapp2_extras import jinja2
from google.appengine.ext import ndb
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users


@app.route('/module/hot_tags', name='hot_tags_module')
def hot_tags_module(request):
    limit = int(request.GET.get('limit'))
    tags = Tags.query().order('-order').fetch(limit)
    return render_template('hot_tags', tags=tags)


# TODO: not use now
@app.route('/module/blog_detail/<blog_str:\w+>', name='detail')
def blog_detail_module(request, blog_str):
    blog = ndb.Key(urlsafe=blog_str).get()
    return render_template('blog_detail', blog=blog)


# TODO: not use now
@app.route('/module/blog_list', name='blog_list')
def blog_list_module(request):
    return render_template('blog_list', blogs=blogs)
