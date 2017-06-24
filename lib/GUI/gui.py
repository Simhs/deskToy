#-*- coding: utf-8 -*-
import math
import thread
import time

import pygame
from pygame.locals import *

from Box2D import *
from random import randint



class GUI:
    def __init__(self):
        # 화면 비율
        self.SCREEN_WD = 800
        self.SCREEN_HT = 480
        # 주사율
        self.TARGET_FPS = 60
        # 거리계
        self.PPM = 20.0
        # 물리엔진 갱신 단위
        self.timeStep = 1.0 / 60
        self.velIters = 10
        self.posIters = 10
        # 색
        self.colors = {
            'wall': (255, 255, 255, 255),
            'water':(000, 000, 255, 255),
            'wood': (102, 051, 000, 150),
        }

        # gui
        self.screen = None

        self.clock = pygame.time.Clock()

        self.font = None
        self.tntImg = None
        self.exploSound = None
        self.fireSound = None

        self.createScreen()
        self.imageload()
        self.fontLoad()
        self.loadSound()

    def createScreen(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WD, self.SCREEN_HT), FULLSCREEN, 32)
        pygame.display.set_caption("PyBox2D-Sim")

    def loadSound(self):
        pygame.mixer.init(48000, -16, 1, 1024)
        self.fireSound = pygame.mixer.Sound("./rsc/fire.wav")

    def play(self,sound):
        pygame.mixer.Sound.play(sound)
        pygame.mixer.music.stop()

    def imageload(self):
        self.tntImg = pygame.image.load('./rsc/tnt.png')
        self.tntImg = pygame.transform.scale(self.tntImg, (40, 40))

    def fontLoad(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def explosionEffect(self,world,tnt):
        bodyList = world.bodyList
        time.sleep(1)
        self.play(self.fireSound)
        for item in bodyList:
            item[0].angularVelocity = 100 #randint(-20, 20)
            item[0].linearVelocity =  b2Vec2(randint(-100, 100), randint(-40, 100))

        for item in bodyList:
            if item[0]==tnt:
                item[1] = 'used'

    def show(self,world):
        self.screen.fill((0, 0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()

        for item in world.bodyList:
            body = item[0]
            if item[1] == 'enter':
                item[1] = 'fire'
                thread.start_new_thread(self.explosionEffect,(world,body))

        for index,item in enumerate(world.bodyList):
            body = item[0]
            if body.position[0] < -5 or body.position[0] > 40:
                world.world.DestroyBody(body)
                world.bodyList.pop(index)
            elif body.position[1] < -2 or body.position[1] > 30:
                world.world.DestroyBody(body)
                world.bodyList.pop(index)
            elif item[1] == 'used':
                world.world.DestroyBody(body)
                world.bodyList.pop(index)

        for item in world.bodyList:
            body = item[0]
            bodyType = item[1]
            if bodyType == "static":
                for fixture in body.fixtures:
                    shape = fixture.shape
                    vertices = [(body.transform * v) * self.PPM for v in shape.vertices]
                    vertices = [(v[0], self.SCREEN_HT - v[1]) for v in vertices]
                    bodyrect = pygame.draw.polygon(self.screen, self.colors['wall'], vertices)

            elif bodyType == "water":
                for fixture in body.fixtures:
                    shape = fixture.shape
                    position = body.transform * shape.pos * self.PPM
                    position = (position[0], self.SCREEN_HT - position[1])
                    pygame.draw.circle(self.screen, self.colors['water'], [int(x) for x in position], int(shape.radius *self.PPM))
            else:
                for fixture in body.fixtures:
                    shape = fixture.shape
                    vertices = [(body.transform * v) * self.PPM for v in shape.vertices]
                    vertices = [(v[0], self.SCREEN_HT - v[1]) for v in vertices]
                    if (-2.0,-1.0) in shape:
                        pygame.draw.polygon(self.screen, self.colors['wood'], vertices)
                        textsurface = self.font.render(item[1], False, (255, 255, 255))
                        rotatedimg = pygame.transform.rotate(textsurface, math.degrees(body.transform.angle))
                        rotatedRect = rotatedimg.get_rect()
                        rotatedRect.center = (
                        body.transform.position[0] * self.PPM, self.SCREEN_HT - body.transform.position[1] * self.PPM)
                        self.screen.blit(rotatedimg, rotatedRect)

                    elif (-1.5,-1.5) in shape:
                        self.tntImg = pygame.transform.scale(self.tntImg, (60, 60))
                        textsurface = self.tntImg
                        rotatedimg = pygame.transform.rotate(textsurface, math.degrees(body.transform.angle))
                        rotatedRect = rotatedimg.get_rect()
                        rotatedRect.center = (
                        body.transform.position[0] * self.PPM, self.SCREEN_HT - body.transform.position[1] * self.PPM)
                        self.screen.blit(rotatedimg, rotatedRect)
                    else:
                        pygame.draw.polygon(self.screen, self.colors['water'], vertices)
                        textsurface = self.font.render(item[1], False, (255, 255, 255))
                        rotatedimg = pygame.transform.rotate(textsurface, math.degrees(body.transform.angle))
                        rotatedRect = rotatedimg.get_rect()
                        rotatedRect.center = (body.transform.position[0]*self.PPM,self.SCREEN_HT - body.transform.position[1]*self.PPM)
                        self.screen.blit(rotatedimg, rotatedRect)

        pygame.display.flip()
        self.clock.tick(self.TARGET_FPS)














