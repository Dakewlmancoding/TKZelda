from tkinter import *
import random

import player
from window import gameWindow
from graphics import Graphics

class Enemy:
    doAi = True
    doUpdateDirection = False
    currentDirection = None
    randomDirectionGenerator = None
    enemyNum = None
    isDead = False
    def __init__(self, n, x, y, tier, drop):
        self.enemyNum = n
        self.xPos = x
        self.yPos = y
        self.tier = tier
        if tier == 0:
            self.health = 1
        elif tier == 1:
            self.health = 2
        elif tier == 2:
            self.health = 3
        self.drop = drop
    def direction(self):
        #randomDirectionGenerator = 1
        if self.doUpdateDirection == True:
            self.randomDirectionGenerator = random.randint(1,4)
            self.doUpdateDirection = False

        if self.randomDirectionGenerator == None:
            self.randomDirectionGenerator = random.randint(1,4)

        if self.randomDirectionGenerator == 1:
            direction = "down"
        elif self.randomDirectionGenerator == 2:
            direction = "up"
        elif self.randomDirectionGenerator == 3:
            direction = "left"
        elif self.randomDirectionGenerator == 4:
            direction = "right"
        #else:
         #    direction = "down"
        #print(randomDirectionGenerator)
        self.currentDirection = direction
        return direction

    count = 0
    def idleWalk(self):
        if self.doAi == True:
            direction = self.direction()
            #print("from idle walk:",direction)
            if self.count < 10:
                if direction == "up":
                    self.yPos -= 10
                elif direction == "down":
                    self.yPos += 10
                elif direction == "right":
                    self.xPos += 10
                elif direction == "left":
                    self.xPos -= 10
                self.count +=1
            if self.count >= 10 and self.count < 15:
                self.count +=1
            if self.count >= 15:
                #print("calling updates")
                self.doUpdateDirection = True
                self.count = 0


    def getSprite(self):
        direction = self.direction()
        #print("from getSprite:", direction)
        sprite = Graphics.guard1Down
        if direction == "down":
            sprite = Graphics.guard1Down
        elif direction == "up":
            sprite = Graphics.guard1Up
        elif direction == "left":
            sprite = Graphics.guard1Left
        elif direction == "right":
            sprite = Graphics.guard1Right
        return sprite

    def canSeePlayer(self):
        direction = self.direction()
        if direction == "down":
            #enemySight = gameWindow.bkgrnd.create_rectangle(self.xPos + 50, self.yPos, self.xPos - 50, self.yPos + 200, tags = "enemySightBox")
            enemyCanSee = gameWindow.bkgrnd.find_overlapping(self.xPos + 50, self.yPos, self.xPos - 50, self.yPos + 200)
        elif direction == "up":
            #enemySight = gameWindow.bkgrnd.create_rectangle(self.xPos + 50, self.yPos, self.xPos - 50, self.yPos - 200, tags = "enemySightBox")
            enemyCanSee = gameWindow.bkgrnd.find_overlapping(self.xPos + 50, self.yPos, self.xPos - 50, self.yPos - 200)
        elif direction == "right":
            #enemySight = gameWindow.bkgrnd.create_rectangle(self.xPos, self.yPos + 50, self.xPos + 200, self.yPos - 50, tags = "enemySightBox")
            enemyCanSee = gameWindow.bkgrnd.find_overlapping(self.xPos, self.yPos + 50, self.xPos + 200, self.yPos - 50)
        elif direction == "left":
            #enemySight = gameWindow.bkgrnd.create_rectangle(self.xPos, self.yPos + 50, self.xPos - 200 - 50, self.yPos - 50, tags = "enemySightBox")
            enemyCanSee = gameWindow.bkgrnd.find_overlapping(self.xPos, self.yPos + 50, self.xPos - 200, self.yPos - 50)
        #print(enemyCanSee)
        playerId = player.Player.playerId(player.Player)
        #print(playerId)
        for i in enemyCanSee:
            if i == playerId:
                #print("I see you!")
                return True
    def chargePlayer(self, player):
        if self.doAi == True:
            playerY = player.yPos
            playerX = player.xPos
            direction = self.direction()
            #print(distanceX,distanceY)
            if direction == "down":
                if self.yPos != playerY:
                    self.yPos += 10
                if self.xPos > playerX:
                    self.xPos -= 10
                elif self.xPos < playerX:
                    self.xPos += 10
                elif self.xPos == playerX:
                    self.xPos = player.xPos
            elif direction == "up":
                if self.yPos != playerY:
                    self.yPos -= 10
                if self.xPos > playerX:
                    self.xPos -= 10
                elif self.xPos < playerX:
                    self.xPos += 10
                elif self.xPos == playerX:
                    self.xPos = player.xPos
            elif direction == "right":
                if self.xPos != playerX:
                    self.xPos += 10
                if self.yPos > playerY:
                    self.yPos -= 10
                elif self.yPos < playerY:
                    self.yPos += 10
                elif self.yPos == playerY:
                    self.yPos = player.yPos
            elif direction == "left":
                if self.xPos != playerX:
                    self.xPos -= 10
                if self.yPos > playerY:
                    self.yPos -= 10
                elif self.yPos < playerY:
                    self.yPos += 10
                elif self.yPos == playerY:
                    self.yPos = player.yPos
    def death(self):
        self.drop.xPos = self.xPos
        self.drop.yPos = self.yPos
        self.xPos = 1100
        self.yPos = 1100
    def hitbox(self):
        gameWindow.bkgrnd.create_rectangle(self.xPos + 30, self.yPos + 40, self.xPos - 30, self.yPos - 40, tags = "enemyHitbox")
    def enemy(self):
        sprite = self.getSprite()
        gameWindow.bkgrnd.create_image(self.xPos, self.yPos, anchor= CENTER, image = sprite, tags ="enemy")
    def enemyId(self):
       enemyIdRAW = gameWindow.bkgrnd.find_withtag("enemy")
       #print(enemyIdRAW)
       return enemyIdRAW[self.enemyNum]