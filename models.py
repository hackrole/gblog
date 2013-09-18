#!/usr/bin/env python
# encoding: utf-8

from google.appengine.ext import ndb


class Category(ndb.Model):
    title = ndb.StringProperty(required=True)
    order = ndb.IntegerProperty(default=10)
    create_time = ndb.DateTimeProperty(auto_now_add=True)


class Tags(ndb.Model):
    title = ndb.StringProperty(required=True)
    create_time = ndb.DateTimeProperty(auto_now_add=True)


class Blog(ndb.Model):
    title = ndb.StringProperty(required=True)
    text = ndb.TextProperty()
    author = ndb.StringProperty(default="hackrole")
    category = ndb.KeyProperty(kind=Category, required=True)
    tags = ndb.KeyProperty(kind=Tags, repeated=True)
    create_time = ndb.DateTimeProperty(auto_now_add=True)
    last_update_time = ndb.DateTimeProperty(auto_now=True)
