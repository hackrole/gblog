#!/usr/bin/env python
# encoding: utf-8

import webapp2
from lib import markdown
from models import Blog, Tag, Category
from google.appengine.api import users
from webapp2_extras import jinja2
from google.appengine.ext.webapp.util import run_wsgi_app


class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render(self, template, **context):
        rv = self.jinja2.render_template(template, **context)
        self.response.write(rv)


class IndexPage(BaseHandler):
    def get(self):
        self.response.write(markdown.markdown(s))
        taglist = Tag.query().fetch()
        catelist = Category.query().fetch()
        blogs = Blog.query().order(-Blog.create_time).fetch(3)
        self.render("index.html", taglist=taglist,
                    catelist=catelist, blogs=blogs)


class PubBLogPage(BaseHandler):
    def get(self):
        # TODO: forms uses
        taglist = Tag.query().fetch()
        catelist = Category.query().fetch()
        self.render("pub.html", taglist=taglist, catelist=catelist)

    def post(self):
        update = self.request.get('update', False)
        cate_name = self.request.get('cate_name')
        tags_list = self.request.get_all('tags_name', [])
        title = self.request.get('title')
        blog = self.request.get('blog')
        if not blog:
            self.response.write('blog content empty!')

        cate = Category.query(Category.title==cate_name).get()
        if not cate:
            cate = Category(title=cate_name)
            cate.put()
        print tags_list
        tags = Tag.query(Tag.title.IN(tags_list)).fetch()
        tags_old = [tag.title for tag in tags]
        tags_new = []
        for tag in tags_list:
            if tag not in tags_old:
                tag = Tag(title=tag)
                tag.put()
                tags_new.append(tag)
        print tags
        print tags_new
        tags += tags_new
        print tags
        print '==='
        print dir(tags[0])
        tags = [tag.key for tag in tags]

        blog = Blog(title=title, text=blog, category=cate.key, tags=tags)
        blog.put()
        self.response.write('blog publish success')
        self.response.set_status(200)


class DetailPage(BaseHandler):
    def get(self, bid):
        blog = Blog.query(Blog.key==bid).fetch()


urls = [
    ('/', IndexPage),
    ('/blog/(\d+)', DetailPage),
    #('/cate/(\d+)', CatePage),
    #('/tag/(\d+)', TagPage),
    ('/pubblog', PubBLogPage),
]
app = webapp2.WSGIApplication(
    urls,
    debug=True
)

if __name__ == '__main__':
    run_wsgi_app(app)
