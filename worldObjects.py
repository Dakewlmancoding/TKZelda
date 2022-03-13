from window import *
from graphics import *


class WorldObjects:
    #type = object type, name = name of the object(for getting sprite), itemDrop = what item to drop (if applicable), subZoneNum = what sub zone to put player in (if applicable), zoneNumY = what Y zone to put player in (if applicable), zoneNumX = what X zone to put player in (if applicable), height/width = dimensions of object for hitbox gen, x/y = coords, num = in order to get id; the nth object generated on screen
    def __init__(self, type, name, itemDrop, subZoneNum, zoneNumX, zoneNumY, height, width, x, y, num):
        self.xPos = x
        self.yPos = y
        self.objectHeight = height
        self.objectWidth = width
        self.name = name
        self.type = type
        if name == "tree1":
            self.sprite = Graphics.tree1
        elif name == "digSpot":
            self.sprite = Graphics.digSpot
            self.isDug = False
            if type == "itemDrop":
                self.itemDrop = itemDrop
            elif type == "warper":
                self.subZoneNum = subZoneNum
                self.zoneNumX = zoneNumX
                self.zoneNumY = zoneNumY
        elif name == "caveWallTop":
            self.sprite = Graphics.caveWallTop
        self.objectNum = num
    def objectHitbox(self):
        gameWindow.bkgrnd.create_rectangle(self.xPos + self.objectWidth, self.yPos + self.objectHeight, self.xPos - self.objectWidth, self.yPos - self.objectHeight, tags = "objectHitbox")
        #print(self.name,"object hitbox drawn")
    def objectImage(self):
        gameWindow.bkgrnd.create_image(self.xPos, self.yPos, anchor = CENTER, image = self.sprite, tags = "object")
        #print(self.name,"object image drawn")
    def objectId(self):
       objectIdRAW = gameWindow.bkgrnd.find_withtag("object")
       #print(objectIdRAW)
       return objectIdRAW[self.objectNum]