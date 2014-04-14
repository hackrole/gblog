#!/usr/bin/env python
# encoding: utf-8
import requests
import setttings


def main():
    base_url = settings.BASE_URL
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
    main()
