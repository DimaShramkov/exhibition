#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

RPI = []
RPI['RPI1'] = ('127.0.0.1', None)
RPI['RPI2'] = ('127.0.0.1', None)
RPI['RPI3'] = ('127.0.0.1', None)
RPI['RPI4'] = ('127.0.0.1', None)
t = True
while t:
    conn, addr = sock.accept()
    for i in RPI:
        if i[0] == addr:
            i[1] == conn
    for i in RPI:
        if i[1] == None:
            t = True
            else t = False

walue = " "
while walue != 'End':
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(4)
    conn, addr = sock.accept()

    print ('connected:', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data.upper())
    conn.close()