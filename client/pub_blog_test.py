#!/usr/bin/env python
# encoding: utf-8
import requests
import settings


def new_tag_test():
    base_url = settings.BASE_URL
    url = ''.join([base_url, '/api/tag/new'])
    post_data = {
        'email': 'daipeng123456@gmail.com',
        'pwd': '123456',
        'title': 'vim',
    }
    if settings.DEBUG:
        response = requests.post(url, post_data)
    else:
        response = requests.post(url, post_data,
                                proxies=settings.PROXY)
    print response
    print response.text


def main():
    base_url = settings.BASE_URL
    url = ''.join([base_url, '/api/blog/new'])
    post_data = {
        'email': 'daipeng123456@gmail.com',
        'pwd': '123456',
        'title': 'vim',
        'content': 'the first blog, the time is now to user vim',
    }

    if settings.DEBUG:
        response = requests.post(url, post_data)
    else:
        response = requests.post(url, post_data,
                                proxies=settings.PROXY)
    print response
    print response.text


if __name__ == '__main__':
    new_tag_test()
    #main()
