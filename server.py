#!/usr/bin/env python

import socket
import argparse
import random
import stun

def server_udp(port=None):

    if not port:
        port = 54000 + random.randint(0,999)
    nat_type, ext_host, ext_port = stun.get_ip_info(source_port=port)
    if nat_type != stun.FullCone:
        print("NAT type should be Full Cone. There is {}".format(nat_type))
        return
    print("start client with parameters:\n\t--host {} --port {}".format(ext_host, ext_port))
    s = socket.socket(type=socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', port))
    while True:
        try:
            data = s.recv(100)
            print(data.encode('utf8'))
            if data == b'Done':
                break
        except socket.timeout:
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-p', '--port', dest='port', help='port', metavar='PORT', type=int)

    args = parser.parse_args()
    server_udp(port=args.port)