#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: generate_github_token.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Sun Oct 25 23:54:41 2015
#########################################################################

import json
import shutil
import urllib
import urllib2
from pprint import pprint
from urllib2 import URLError

token_file_uri = 'access_token.txt'

def generate_github_token():
    try:
        url = 'https://api.github.com/authorizations'
        values = {
            'scopes' : ["public_repo"],
            'note' : 'robot script'
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        print response.status,response.reason
        the_page = response.read()
        data_json = json.loads(the_page)
        pprint(data_json)
        in_fqueue(token_file_uri, data_json['token'])
    except URLError, e:
        print 'Network Error'
        pprint(e)

def pull_token():
    return de_fqueue(token_file_uri)

def en_fqueue(file_uri, line):
    with open(file_uri, 'a') as f:
        f.write(line)

def de_fqueue(file_uri):
    file_uri_tmp = file_uri + '.tmp'
    with open(file_uri, 'rw') as f:
        first_line = f.readline()
        with open(file_uri_tmp, 'w') as f_tmp:
            for line in f:
                f_tmp.write(line)
    shutil.move(file_uri_tmp, file_uri)
    return first_line

if __name__ == '__main__':
    generate_github_token()
