#!/usr/bin/env python
# encoding: utf-8

import re
import sys
import requests


def parse_org_file(fn):
    assert os.path.exists(fn), "%s not exists" % f
    data = {}
    data['email'] = settings.ADMIN_EMAIL
    data['pwd'] = settings.ADMIN_PWD
    with open(fn) as f:
        data['text'] = f.read()
        data['title'] = re.findall(settings.TITLE_R, text)
        data['tags'] = re.findall(settings.TAGS_REG, text)
        data["content"] = text

    return data


def main():
    fn = sys.args[1]
    base_url = settings.BASE_URL
    url = ''.join([base_url, '/api/blog/new'])
    post_data = parse_org_file(fn)

    response = requests.post(url, post_data)
    print response.status_code
    if setttings.DEBUG:
        print response.text
