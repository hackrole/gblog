#!/usr/bin/env python
# encoding: utf-8

import json
from google.appengine.ext import ndb


class Category(ndb.Model):
    title = ndb.StringProperty(required=True)
    order = ndb.IntegerProperty(default=10)
    create_time = ndb.DateTimeProperty(auto_now_add=True)


class Tag(ndb.Model):
    title = ndb.StringProperty(required=True)
    create_time = ndb.DateTimeProperty(auto_now_add=True)


class Blog(ndb.Model):
    title = ndb.StringProperty(required=True)
    content = ndb.TextProperty()
    author = ndb.StringProperty(default="hackrole")
    category = ndb.KeyProperty(kind=Category)
    tags = ndb.KeyProperty(kind=Tag, repeated=True)
    create_time = ndb.TimeProperty(auto_now_add=True)
    update_time = ndb.TimeProperty(auto_now=True)

    def to_json(self):
        return json.dumps({
            'id': self.key.urlsafe(),
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'category_id': self.category.urlsafe(),
            'tags_id': [tag.urlsafe() for tag in self.tags],
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%s'),
            'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%s'),
        })


class Wiki(ndb.Model):
    title = ndb.StringProperty(required=True)
    create_time = ndb.DateTimeProperty(auto_now_add=True)
    update_time = ndb.DateTimeProperty(auto_now=True)


class Book(ndb.Model):
    title = ndb.StringProperty(required=True)
    download_urls = ndb.StringProperty() # TODO: string to list
    buy_urls = ndb.StringProperty()
    create_time = ndb.DateTimeProperty(auto_now_add=True)
    update_time = ndb.DateTimeProperty(auto_now=True)


class Admin(ndb.Model):
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    create_time = ndb.DateTimeProperty(auto_now_add=True)
