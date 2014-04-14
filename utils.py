#!/usr/bin/env python
# encoding: utf-8
import requests

def blog_new_client():
    base_url = "http://localhost:8080"
    url = ''.join([base_url, '/api/blog/new'])
    post_data = {
        'email': 'daipeng123456@gmail.com',
        'pwd': '123456',
        'title': 'emacs',
        'content': 'the first blog',
    }

    response = requests.post(url, post_data)
    print response
    print response.text


if __name__ == '__main__':
    blog_new_client()
