from window import *
from graphics import *
from player import *
from item import *
from enemy import *
from worldObjects import *

import random


class World:
    def __init__(self):
        self.worldBottom = 1000
        self.worldTop = 0
        self.worldRight = 1000
        self.worldLeft = 0

        #Which zone the player is in
        self.zoneX = 0
        self.zoneY = 0
        self.subZone = 0 #0=overworld, 1=cave
        #Current zone info
        self.currentZoneItems = []
        self.currentZoneEnemies = []
        self.currentZoneObjects = []
        self.currentZone = None
#reminder: (self, type, name, itemDrop, subZoneNum, zoneNumX, zoneNumY, height, width, x, y, num)

#Test Zone info
    zTItems = []
    zTObjects = []
    zTEnemies = []
    zoneTest = [zTObjects, zTItems, zTEnemies]

#Test Zone Two info
    zT2EnemyDrop= Item("heal", "heartPickup", 8, 8, 1100, 1100, 0)
    zT2Enemy2Drop = Item("heal", "heartPickup", 8,8, 1100, 1100, 1)
    zT2Enemy = Enemy(0, 300, 500, 1, zT2EnemyDrop)
    zT2Enemy2 = Enemy(1, 800, 500, 1, zT2Enemy2Drop)
    zT2Tree = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 200, 200, 0)
    zT2Tree2 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 900, 200, 1)
    zT2Items = [zT2EnemyDrop, zT2Enemy2Drop]
    zT2Objects = [zT2Tree, zT2Tree2]
    zT2Enemies = [zT2Enemy, zT2Enemy2]
    zoneTest2 = [zT2Objects, zT2Items, zT2Enemies]

#Overworld Zone 0,0 info
    over00Tree = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 200, 200, 0)
    over00Tree2 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 800, 600, 1)
    over00Items = []
    over00Objects = [zT2Tree, zT2Tree2]
    over00Enemies = []
    zone00 = [over00Objects, over00Items, over00Enemies]

#Overworld Zone 0,1 info
    over01Tree = WorldObjects("tree", "tree1", None, None, None, None, 100, 100, 100, 100, 0)
    over01Tree3 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 400, 100, 2)
    over01Tree2 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 250, 100, 1)
    over01Tree4 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 550, 100, 3)
    over01Tree5 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 700, 100, 4)
    over01Tree6 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 850, 100, 5)
    over01Tree7 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 1000, 100, 6)
    over01Tree8 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 100, 100, 7)
    over01Tree9 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 50, 250, 8)
    over01Tree10 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 50, 400, 9)
    over01Tree11 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 50, 550, 10)
    over01Tree12 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 50, 700, 11)
    over01Tree13 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 50, 850, 12)
    over01Tree14 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 50, 1000, 13)
    over01Tree15 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 100, 100, 14)
    over01Tree16 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 950, 250, 15)
    over01Tree17 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 950, 400, 16)
    over01Tree18 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 950, 550, 17)
    over01Tree19 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 950, 700, 18)
    over01Tree20 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 950, 850, 19)
    over01Tree21 = WorldObjects("tree", "tree1",None, None, None, None, 100, 100, 950, 1000, 20)
    over01DigSpot = WorldObjects("warper", "digSpot",None, 1, 0, 0, 128, 128, 500, 400, 21)
    over01Shovel = Item("shovel", "shovel", 16, 16, 500, 500, 0)
    over01Items = [over01Shovel]
    over01Objects = [over01Tree, over01Tree2, over01Tree3, over01Tree4, over01Tree5, over01Tree6, over01Tree7, over01Tree8, over01Tree9, over01Tree10, over01Tree11, over01Tree12, over01Tree13, over01Tree14, over01Tree15, over01Tree16, over01Tree17, over01Tree18, over01Tree19, over01Tree20, over01Tree21, over01DigSpot]
    over01Enemies = []
    zone01 = [over01Objects, over01Items, over01Enemies]

#Cave Zone 1,1
    cave11Wall = WorldObjects("wall", "caveWallTop", None, None, None, None, 100, 100, 100, 100, 0)
    cave11Items = []
    cave11Objects = [cave11Wall]
    cave11Enemies = []
    cavezone11 = [cave11Objects, cave11Items, cave11Enemies]


#functions n' such
    doLoadZone = False
    #Gets what zone the player is in
    def checkZone(self):
        if self.subZone == 0:
            if (self.zoneX == 0) and (self.zoneY == 0):
                self.currentZone = self.zone00
            elif (self.zoneX == 0) and (self.zoneY == 1):
                self.currentZone = self.zone01
            else:
                self.currentZone = self.zoneTest2
        elif self.subZone == 1:
            if (self.zoneX == 0) and (self.zoneY == 0):
                self.currentZone = self.cavezone11
            else:
                self.currentZone = self.zoneTest2
    #generates the world around the player
    def loadZone(self):
        print(self.zoneX, self.zoneY)
        self.currentZoneItems = []
        self.currentZoneEnemies = []
        self.currentZoneObjects = []
        x = self.worldBottom
        y = self.worldRight
        self.checkZone()
        while (y >= -1152) == True:
            while (x >= -1152) == True:
                if self.subZone == 0:
                    ground = Graphics.groundNorm
                elif self.subZone == 1:
                    ground = Graphics.groundCave
                gameWindow.bkgrnd.create_image(x, y, anchor = SE, image = ground)
                x -= 192
            y -= 192
            x = 1000
        #detail generation
        columnNum = 4 #number of columns detail gen is split into
        xMin = 1000
        xMax= 750
        while columnNum != 0:
            miscNum = 12 #number of details to generate per column
            while miscNum >= 0:
                ranY = random.randint(0, 1000)
                ranX = random.randint(xMax, xMin)
                gameWindow.bkgrnd.create_image(ranX, ranY, anchor = CENTER, image = Graphics.grass)
                #print("misc detail generated at", ranX, ranY)
                #print(miscNum)
                miscNum -= 1
            xMin -= 250
            xMax -= 250
            columnNum -=1
        #specific object generation
        objects = self.currentZone[0]
        items = self.currentZone[1]
        enemies = self.currentZone[2]
        #print("From World:", objects,enemies,items)
        for e in enemies:
            self.currentZoneEnemies.append(e)
        for i in items:
            self.currentZoneItems.append(i)
        for o in objects:
            self.currentZoneObjects.append(o)



#obsolete(?)
    def newZone(self):
        x = self.worldBottom
        y = self.worldRight
        while (y >= -1152) == True:
            while (x >= -1152) == True:
                gameWindow.bkgrnd.create_image(x, y, anchor = SE, image = Graphics.groundNorm)
                x -= 192
            y -= 192
            x = 1000
        #detail generation
        columnNum = 4 #number of columns detail gen is split into
        xMin = 1000
        xMax= 750
        while columnNum != 0:
            miscNum = 12 #number of details to generate per column
            while miscNum >= 0:
                ranY = random.randint(0, 1000)
                ranX = random.randint(xMax, xMin)
                gameWindow.bkgrnd.create_image(ranX, ranY, anchor = CENTER, image = Graphics.grass)
                #print("misc detail generated at", ranX, ranY)
                #print(miscNum)
                miscNum -= 1
            xMin -= 250
            xMax -= 250
            columnNum -=1
