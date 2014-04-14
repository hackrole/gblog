#!/usr/bin/env python
# encoding: utf-8

import re
import sys
import os
import requests
import settings


def parse_org_file(fn):
    assert os.path.exists(fn), "%s not exists" % fn
    data = {}
    data['email'] = settings.ADMIN_EMAIL
    data['pwd'] = settings.ADMIN_PWD
    with open(fn) as f:
        text = f.read()
        print text
        data['title'] = re.findall(settings.TITLE_REG, text)[0]
        #data['tags'] = re.findall(settings.TAGS_REG, text)[0]
        data["content"] = text
    print data

    return data


def main():
    fn = sys.argv[1]
    base_url = settings.BASE_URL
    url = ''.join([base_url, '/api/blog/new'])
    post_data = parse_org_file(fn)

    response = requests.post(url, post_data,
                             proxies=settings.PROXY)
    print response.status_code
    if settings.DEBUG:
        print response.text

if __name__ == '__main__':
    main()
