from window import *
from graphics import *


class Item:
    #type = item type (NYI), name = name of the item(for getting sprite), height/width = dimensions of item for hitbox gen, x/y = coords, num = in order to get id; the nth item generated on screen
    def __init__(self, type, name, height, width, x, y, num):
        self.xPos = x
        self.yPos = y
        self.itemHeight = height
        self.itemWidth = width
        self.name = name
        if name == "sword1":
            self.sprite = Graphics.sword1
        elif name == "heartPickup":
            self.sprite = Graphics.heartPickup
        elif name == "shovel":
            self.sprite = Graphics.shovel
        self.itemNum = num
    def itemHitbox(self):
        gameWindow.bkgrnd.create_rectangle(self.xPos + self.itemWidth, self.yPos + self.itemHeight, self.xPos - self.itemWidth, self.yPos - self.itemHeight, tags = "itemHitbox")
        #print(self.name,"item hitbox drawn")
    def itemImage(self):
        gameWindow.bkgrnd.create_image(self.xPos, self.yPos, anchor = CENTER, image = self.sprite, tags = "item")
        #print(self.name,"item image drawn")
    def itemId(self):
       itemIdRAW = gameWindow.bkgrnd.find_withtag("item")
       #print(itemIdRAW)
       return itemIdRAW[self.itemNum]