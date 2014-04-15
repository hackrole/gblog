#!/usr/bin/env python
# encoding: utf-8

import webapp2
from models import Blog, Tag, Admin
from jinja2 import Environment, FileSystemLoader


def admin_auth(request):
    """
    temp auth for admin,
    TODO: user the google auth instead
    """
    email = request.params.get('email', '')
    pwd = request.params.get('pwd', '')
    if not Admin.auth(email, pwd):
        webapp2.abort(401, "admin required")
    return True


def render_template(template, **kw):
    """
    TODO: cached the env
    """
    env = Environment(
        loader=FileSystemLoader(settings.TEMPLATES_DIR))
    hot_tags = Tag.query().order(
        -Tag.order).fetch(settings.HOT_TAGS_MODULE_PAGE_SIZE)
    recent_comments = []
    global_var = {'settings': settings,
                  'hot_tags': hot_tags,
                  'recent_comments': recent_comments}
    template = env.get_template(template, globals=global_var)
    return template.render(**kw)


