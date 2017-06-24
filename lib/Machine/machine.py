#-*- coding: utf-8 -*-
import thread
from lib.Server.serv import *
import thread

from lib.Server.serv import UDPserver
from lib.GUI.gui import GUI
from lib.PhysicalEngine.physicalengine import World
from random import randint

class Machine:
    def __init__(self):
        # 객체들
        self.world = None
        self.udpserv = None
        self.gui = None

        # 물리엔진 갱신시 필요한 파라메타
        self.posIters = None
        self.velIters = None
        self.timeStep = None

    def start(self):
        # 객체 생성
        self.udpserv = UDPserver(self)
        self.gui = GUI()
        self.world = World()

        # 물리엔진 갱신시 필요 파라메터 (GUI에 의존)
        self.posIters = self.gui.posIters
        self.velIters = self.gui.velIters
        self.timeStep = self.gui.timeStep

        thread.start_new_thread(self.udpserv.recv, ())
        self.world.addStaticBoxOnWorld(14,1,14,1)
        self.world.addStaticBoxOnWorld(38, 1, 2, 1)
        self.world.addStaticBoxOnWorld(39, 12, 1, 12)
        self.world.addStaticBoxOnWorld(1, 12, 1, 12)
        self.world.addStaticBoxOnWorld(3, 6, 1, 6)
        self.world.addStaticBoxOnWorld(2, 17, 1, 5)

    def interrupt(self,msg):
        p_key = str(msg)
        x_pos = randint(10,30)
        x_vector = randint(-10,10)
        y_vector = randint(15, 30)
        spin = randint(-10, 10)

        if 'Key' in p_key:
            key_name = p_key.replace('Key.', '')
            if key_name == "enter":
                self.world.addEnterKeyBoxOnWorld(x=x_pos, y=5, w=1.5, h=1.5, linearVelocity=(x_vector, y_vector), angularVelocity=spin,key_name=key_name)
            else:
                self.world.addKeyBoxOnWorld(x=x_pos,y=5,w=2,h=1,linearVelocity=(x_vector,y_vector),angularVelocity=spin,key_name=key_name)

        else:
            key_name = p_key.replace('u', '').replace("\'", '')
            print key_name
            self.world.addKeyBoxOnWorld(x=x_pos,y=5,w=1,h=1,linearVelocity=(x_vector,y_vector),angularVelocity=spin,key_name=key_name)

    def waterfull(self):
        self.world.addCircleOnWorld(x=x_pos, y=5, r=1, linearVelocity=(x_vector, y_vector), angularVelocity=spin, key_name="water")

    def showWord(self):
        # world 상태 보여주기
        self.gui.show(self.world)

    def updateWord(self):
        # world 상태 갱신
        self.world.world.Step(self.timeStep, self.velIters, self.posIters)


'''
if __name__=="__main__":
    game = Machine()
    world = game.start()
    while True:
        game.showWord(world)
        game.updateWord(world)
'''


