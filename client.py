#!/usr/bin/env python

import socket

import argparse

def client_udp(*addr):

    s = socket.socket(type=socket.SOCK_DGRAM)
    for i in range(100):
        s.sendto(b'Hello world\n', addr)
    for i in range(3):
        s.sendto(b'Done', addr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Укажате параметры выданные сервером:")
    parser.add_argument('-p', '--port', dest='port', help='port', metavar='PORT', type=int)
    parser.add_argument('-H', '--host', dest='host', help='host', metavar='HOST')

    args = parser.parse_args()
    if not args.port or not args.host:
        parser.print_help()
    else:
        client_udp(args.host, args.port)