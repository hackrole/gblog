#!/usr/bin/env python
# encoding: utf-8

# the file give the needed settings for the client

DEBUG = True

# auth required
ADMIN_EMAIL = "daipeng123456@gmail.com"
ADMIN_PWD = "123456"

# BASE_URL for client request
BASE_URL = "http://localhost:8080" # for test
#BASE_URL = "http://hr-note.appspot.com"

# org re conf
TITLE_REG = "#\+TITLE:\s*(.+)\n"
TAGS_REG = "#\+TAGS:\s*(.+)\n"

# proxy setting to avoid GFW
USE_PROXY = True
PROXY = {
    "http": "http://127.0.0.1:8087",
    "https": "http://127.0.0.1:8087",
}
