#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import requests
# import json
# import http.client
from urllib.parse import quote_plus
import socket

api = 'http://restapi.amap.com/v3/geocode/geo'
key = 'f5d0edf7a783d6f954906d91c3453549'
address = u'北京市朝阳区'

request_text = """\
    GET /v3/geocode/geo?key={}&address={} HTTP/1.1\r\n\
    Host: restapi.amap.com:80\r\n\
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36\r\n\
    Connection: close\r\n\
    \r\n\
    """

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'


def geocode(address):
    sock = socket.socket()
    sock.connect(('restapi.amap.com', 80))

    request = request_text.format(key, quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))


# def geocode(address):
#     path = '{}?key={}&address={}'.format(api, key, quote_plus(address))
#     connection = http.client.HTTPConnection('restapi.amap.com')
#     connection.request('GET', path)
#     rawreply = connection.getresponse().read()
#     result = json.loads(rawreply.decode('utf-8'))
#     answer = result['geocodes'][0]['location']
#     print(answer)

# def geocode(address):
#     parameters = {'address': address, 'key': key, 'output': 'JSON'}
#     base = api
#     response = requests.get(base, params=parameters)
#     result = json.loads(response.content.decode('utf-8'))
#     answer = result['geocodes'][0]['location']
#     print(answer)


if __name__ == '__main__':
    geocode(address)
