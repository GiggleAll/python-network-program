#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import socket
import sys
import random

MAX_BYTES = 65535


def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('Listening at', sock.getsockname())
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random() < 0.5:
            print('Pretending to drop packet from {}'.format(address))
            continue
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        message = 'You data was {} bytes long'.format(len(data))
        sock.sendto(message.encode('ascii'), address)


def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    print(hostname)
    sock.connect((hostname, port))
    print('Client socket name is {}'.format(sock.getsockname()))

    delay = 0.1
    text = 'This is another message'
    data = text.decode('ascii')
    while True:
        sock.send(data)
        print('Waiting up to {} seconds for a reply'.format(delay))
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except sock.timeout:
            delay *= 2
            if delay > 2.0:
                raise RuntimeError('I think the server is down')
        else:
            break
        print('The server say {!r}'.format(data.decode('ascii')))


if __name__ == '__main__':
    pass
