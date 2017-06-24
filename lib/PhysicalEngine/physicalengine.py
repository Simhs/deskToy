from random import randint
from Box2D import *
from lib.PhysicalEngine.gameobject import *

class World:
    def __init__(self):
        self.world = b2World(gravity=(0, -20), doSleep=True)
        self.bodyList = []

    def getWorld(self):
        return  self.world

    def addKeyBoxOnWorld(self, x=10, y=10, w=1, h=1, linearVelocity=(0, 20), angularVelocity=5,key_name="str"):
        rect = RectBody(self.world,x= x, y = y, w =w , h=h,linearVelocity=linearVelocity,angularVelocity=angularVelocity)
        rect.addOnWord()
        self.bodyList.append([rect.getBody(),str(key_name)])

    def addEnterKeyBoxOnWorld(self, x=10, y=10, w=1.5, h=1.5, linearVelocity=(0, 20), angularVelocity=5,key_name="str"):
        rect = RectBody(self.world,x= x, y = y, w =w , h=h,linearVelocity=linearVelocity,angularVelocity=angularVelocity)
        rect.addOnWord()
        self.bodyList.append([rect.getBody(), str(key_name)])

    def addCircleOnWorld(self, x= 40, y = 1,r =1,linearVelocity=(0, 20), angularVelocity=5,key_name="str"):
        corcle = CircleBody(self.world,x= x, y = y,r = r,linearVelocity=linearVelocity,angularVelocity=angularVelocity)
        corcle.addOnWord()
        self.bodyList.append([corcle.getBody(), str(key_name)])

    def addStaticBoxOnWorld(self, x= 40, y = 1, w =1 , h=1):
        static = StaticBody(self.world,x= x, y = y, w =w , h=h)
        static.addOnWord()
        self.bodyList.append([static.getBody(), str("static")])