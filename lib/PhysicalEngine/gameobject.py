from Box2D import *
from random import randint

class GameObject:

    world = None
    bodyDef = None
    fixtureDef = None
    shape = None
    body = None
    image = None
    createSound = None
    distroySound = None



class CircleBody(GameObject):
    def __init__(self, world, x=10, y=10, r=1, linearVelocity=(5, 5), angularVelocity=5):
        self.world = world
        self.x = x
        self.y = y
        self.r=r
        self.linearVelocity = linearVelocity
        self.angularVelocity = angularVelocity
        self.defineBody()

        self.body = None

    def defineBody(self):
        self.bodyDef = b2BodyDef()
        self.bodyDef.type = b2_dynamicBody
        self.bodyDef.position.Set(self.x, self.y)
        self.bodyDef.angle = 0
        self.bodyDef.angularVelocity = self.angularVelocity
        self.bodyDef.linearVelocity = self.linearVelocity

        self.shape = b2CircleShape()
        self.shape.radius = self.r

        self.fixtureDef = b2FixtureDef()
        self.fixtureDef.shape = self.shape
        self.fixtureDef.density = 1
        self.fixtureDef.linearDamping = 10
        self.fixtureDef.friction = 0.3

    def addOnWord(self):
        self.body = self.world.CreateBody(self.bodyDef)
        self.body.CreateFixture(self.fixtureDef)

    def getBody(self):
        return self.body

class RectBody(GameObject):
    def __init__(self,world,x=10,y=10,w=1,h=1,linearVelocity=(5,5),angularVelocity=5):
        self.world = world
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.linearVelocity = linearVelocity
        self.angularVelocity = angularVelocity
        self.defineBody()

        self.body = None

    def defineBody(self):

        self.bodyDef = b2BodyDef()
        self.bodyDef.type = b2_dynamicBody
        self.bodyDef.position.Set(self.x, self.y)
        self.bodyDef.angle = 0
        self.bodyDef.angularVelocity = self.angularVelocity
        self.bodyDef.linearVelocity = self.linearVelocity

        self.shape = b2PolygonShape()
        self.shape.SetAsBox(self.w, self.h)

        self.fixtureDef = b2FixtureDef()
        self.fixtureDef.shape = self.shape
        self.fixtureDef.density = 0.3
        self.fixtureDef.friction = 0.3



    def addOnWord(self):
        self.body = self.world.CreateBody(self.bodyDef)
        self.body.CreateFixture(self.fixtureDef)

    def getBody(self):
        return  self.body

class StaticBody(GameObject):

    def __init__(self,world,x=10,y=10,w=1,h=1):
        self.world = world
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.defineBody()

    def defineBody(self):
        self.bodyDef = b2BodyDef()
        self.bodyDef.position.Set(self.x, self.y)
        self.shape = b2PolygonShape()
        self.shape.SetAsBox(self.w, self.h)

    def addOnWord(self):
        self.body = self.world.CreateBody(self.bodyDef)
        self.body.CreateFixture(shape=self.shape)

    def getBody(self):
        return  self.body

class decorator(GameObject):
    gameObject = None

class explosion(decorator):
    def __init__(self, gameObject):
        self.gameObject = gameObject
        self.blast()

    def blast(self):
        angularVelocity = randint(-20,20)
        linearVelocity = (randint(-50,50),randint(-50,50))
