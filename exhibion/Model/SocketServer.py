#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from threading import Thread

class Server:

    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('', 9090))
        self.sock.listen(4)
        self.RPI = {}
        # RPI['RPI1'] = ('127.0.0.1', None)
        self.RPI['RPI2'] = ['192.168.1.56', None]
        self.RPI['RPI3'] = ['192.168.1.171', None]
        # RPI['RPI4'] = ('127.0.0.1', None)

    def connect(self):
        print(len(self.RPI))
        te = 0
        while te != len(self.RPI):
            conn, addr = self.sock.accept()

            for i in self.RPI:
                print(self.RPI[i][0])
                if self.RPI[i][0] == addr[0]:
                    self.RPI[i][1] = conn
                    te += 1
                    print(te)
                    print(addr[0])
            print(self.RPI)
        while True:
            data = conn.recv(1024)

    def run_video(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"run_video")

    def stop_video(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"stop_video")

    def disconnect(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"disconnect")

    def run_projector(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"run_projector")

    def stop_projector(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"stop_projector")

    def run_monitor1(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"run_monitor1")

    def stop_monitor1(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"stop_monitor1")

    def run_monitor2(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"run_monitor2")

    def stop_monitor2(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"stop_monitor2")

    def run_monitor3(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"run_monitor3")

    def stop_monitor3(self):
            for i in self.RPI:
                self.RPI[i][1].send(b"stop_monitor3")
