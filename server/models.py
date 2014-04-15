#!/usr/bin/env python
# encoding: utf-8

import json
from datetime import time as dtime
from google.appengine.ext import ndb


def _switch_ndbProperty_type_to_jsonable(k, v):
    """ swtich ndb property type and return jsonable value """
    if isinstance(v, ndb.key.Key):
        return (k, v.urlsafe())
    elif isinstance(v, dtime):
        return (k, v.strftime('%Y-%m-%d %H:%M:%S'))
    elif isinstance(v, list):
        pass

    return (k, v)


class BaseModel(ndb.Model):
    def to_json(self):
        to_dict = self.to_dict()
        jsonable_tuple = map(_switch_ndbProperty_type_to_jsonable,
                            to_dict.keys(), to_dict.values())

        return dict(jsonable_tuple)

    def to_json_str(self):
        return json.dumps(self.to_json())

    @classmethod
    def get_by_urlsafe(cls, urlsafe):
        return ndb.Key(urlsafe=urlsafe).get()


class Tag(BaseModel):
    title = ndb.StringProperty(required=True)
    order = ndb.IntegerProperty(default=10)
    create_time = ndb.TimeProperty(auto_now_add=True)

    def delete(self):
        raise Exception("unable to delete")


class Blog(BaseModel):
    title = ndb.StringProperty(required=True)
    content = ndb.TextProperty()
    tags = ndb.KeyProperty(kind=Tag, repeated=True)
    create_time = ndb.TimeProperty(auto_now_add=True)
    update_time = ndb.TimeProperty(auto_now=True)
    is_delete = ndb.BooleanProperty(default=False)

    def delete(self):
        self.is_delete = True
        self.put()


class Admin(BaseModel):
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    create_time = ndb.TimeProperty(auto_now_add=True)

    @classmethod
    def auth(cls, email, pwd):
        if cls.query(Admin.email==email, Admin.password==pwd).get():
            return True
        return False
