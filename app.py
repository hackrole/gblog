#!/usr/bin/env python
# encoding: utf-8

import blog


urls = [
]


app = webapp2.WSGIApplication(
    urls,
    debug=True
)

if __name__ == '__main__':
    run_wsgi_app(app)
