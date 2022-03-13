import keyboard

from graphics import *
from window import *

class Inventory:
    isOpen = False
    def checkOn(self):
        if keyboard.is_pressed("b") == True:
            if self.isOpen == False:
                self.isOpen = True
            elif self.isOpen == True:
                self.isOpen = False

    def itemInventoryHandler(self, playerInstance):
        gameWindow.bkgrnd.create_image(50 ,100 , anchor = NW, image = Graphics.itemInventory, tags = "itemInventory")
        if playerInstance.hasShovel == True:
            gameWindow.bkgrnd.create_image(85, 134, anchor = NW, image = Graphics.shovel, tags = "itemInventoryItem")
