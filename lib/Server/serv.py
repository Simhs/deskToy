#-*- coding: utf-8 -*-

from socket import *

class UDPserver:
    def __init__(self,machine):
        self.svrsock = socket(AF_INET, SOCK_DGRAM)
        self.svrsock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.svrsock.bind(('', 5001))  # 로컬호스트에 5001포트로 바인딩
        self.machine = machine

    def recv(self):
        while True:
            msg,_= self.svrsock.recvfrom(15)
            self.machine.interrupt(msg)