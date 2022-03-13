import keyboard
from tkinter import *

from window import gameWindow
from graphics import Graphics
class Console: #the cheat terminal
    isOn = False
    gm = False #invulnerability (God Mode)
    doAi = True
    changeZone = False
    zoneDim = "o"
    zoneX = 0
    zoneY = 0
    consoleText = ""
    consoleTextOut =""
    checkCommand = False

    #items for give command
    giveSword = False
    giveShovel = False

    def checkOn(self):
        if keyboard.is_pressed("`") == True:
            if self.isOn == False:
                self.isOn = True
            elif self.isOn == True:
                self.isOn = False
                self.consoleText = ""
                self.consoleTextOut = ""


    def tgm(self):
        if self.gm == False:
            self.gm = True
            self.consoleTextOut = "God Mode Enabled"
        elif self.gm == True:
            self.gm = False
            self.consoleTextOut = "God Mode Disabled"

    def tai(self):
        if self.doAi == True:
            self.doAi = False
            self.consoleTextOut = "AI Disabled"
        elif self.doAi == False:
            self.doAi = True
            self.consoleTextOut = "AI Enabled"

    def give(self):
        itemStr = self.consoleText[:0] + self.consoleText[5:]
        if itemStr == "sword":
            self.giveSword = True
        elif itemStr == "shovel":
            self.giveShovel = True
        self.consoleTextOut = "Given " + itemStr
        print(itemStr)
    
    #Z, x, y; Z=zonedim
    def setZone(self):
        self.changeZone = True
        zoneVarsStr = self.consoleText[:0] + self.consoleText[3:]
        zoneVars = zoneVarsStr.split(", ")
        self.zoneDim = zoneVars[0]
        self.zoneX = zoneVars[1]
        self.zoneY = zoneVars[2]

    def consoleListener(self):
            if keyboard.is_pressed("Enter") == True:
                self.checkCommand = True
            if keyboard.is_pressed("Backspace") == True:
                self.consoleText = self.consoleText[:-1]
            elif keyboard.is_pressed('t') == True:
                self.consoleText += 't'
            elif keyboard.is_pressed('Space') == True:
                self.consoleText += ' '
            elif keyboard.is_pressed('comma') == True:
                self.consoleText += ','
            elif keyboard.is_pressed('g') == True:
                self.consoleText += 'g'
            elif keyboard.is_pressed('m') == True:
                self.consoleText += 'm'
            elif keyboard.is_pressed('a') == True:
                self.consoleText += 'a'
            elif keyboard.is_pressed('i') == True:
                self.consoleText += 'i'
            elif keyboard.is_pressed('0') == True:
                self.consoleText += '0'
            elif keyboard.is_pressed('1') == True:
                self.consoleText += '1'
            elif keyboard.is_pressed('v') == True:
                self.consoleText += 'v'
            elif keyboard.is_pressed('e') == True:
                self.consoleText += 'e'
            elif keyboard.is_pressed('s') == True:
                self.consoleText += 's'
            elif keyboard.is_pressed('z') == True:
                self.consoleText += 'z'
            elif keyboard.is_pressed('w') == True:
                self.consoleText += 'w'
            elif keyboard.is_pressed('c') == True:
                self.consoleText += 'c'
            elif keyboard.is_pressed('o') == True:
                self.consoleText += 'o'
            elif keyboard.is_pressed('r') == True:
                self.consoleText += 'r'
            elif keyboard.is_pressed('d') == True:
                self.consoleText += 'd'
            elif keyboard.is_pressed('h') == True:
                self.consoleText += 'h'
            elif keyboard.is_pressed('l') == True:
                self.consoleText += 'l'
    def consoleInput(self):
        consoleBox = gameWindow.bkgrnd.create_image(0,700, anchor = NW, image = Graphics.consoleWindow, tags = "consoleWindow")
        consoleTextBox = gameWindow.bkgrnd.create_text(10,725,anchor = NW, text = self.consoleText, fill = "white", font = Graphics.consoleFont, tags = "consoleText")
        consoleTextOutBox = gameWindow.bkgrnd.create_text(10,710,anchor = NW, text = self.consoleTextOut, fill = "white", font = Graphics.consoleFont, tags = "consoleText")

        self.consoleListener()
        if self.checkCommand == True:
            if self.consoleText == 'tgm':
                self.tgm()
            elif self.consoleText == 'tai':
                self.tai()
            elif "give" in self.consoleText:
                self.give()
            elif "sz" in self.consoleText:
                self.setZone()
            self.consoleText = ""
            self.checkCommand = False



