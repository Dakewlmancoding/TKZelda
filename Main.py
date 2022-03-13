#Jack Bell
#oh boy, here we goooooooo!
#Basically a Zelda clone




#Last modified 10/10/2020
#Imports

#Internals
from player import Player
from world import World
from window import gameWindow
from graphics import Graphics
from enemy import Enemy
from console import Console
from inventory import Inventory
from item import Item
from collision import Collision
from worldObjects import WorldObjects

#py Modules
from tkinter import *
import random
import keyboard


#Define Variables

#creates new instances of classes
c = Console()
i = Inventory()
col = Collision()
p = Player()
w = World()
gW = gameWindow

enemies = []
items = []
objects = []

#updates the enemies
def updateEnemies(enemies, objects):
    gameWindow.bkgrnd.delete("enemy", "enemySightBox", "enemyHitbox")
    for i in enemies:
        #i.hitbox()
        i.enemy()
        if i.health == 0 and i.isDead == False:
            i.death()
            i.doAi = False
            i.isDead = True
            #print(drop.name)
        if i.canSeePlayer() == True:
            i.chargePlayer(p)
            #print("I see you!")
        else:
            if i.yPos >= 970 and i.currentDirection =="down":
                i.doUpdateDirection = True
            elif i.yPos <= 30 and i.currentDirection == "up":
                i.doUpdateDirection = True
            elif i.xPos >= 970 and i.currentDirection == "right":
                i.doUpdateDirection = True
            elif i.xPos <= 30 and i.currentDirection == "left":
                i.doUpdateDirection = True
            else:
                i.idleWalk()
        col.collision(i,p, w)
        for o in objects:
            col.collision(o, i, w)
        #print(e.count)
    #print("enemy x =", e.xPos)
    #print("player x =", p.xPos)

#updates the player's values
def updatePlayer(enemies):
    gameWindow.bkgrnd.delete("player", "playerHitbox", "heartFull", "heartHalf", "heartEmpty", "swordSweepBox", "playerSword")
    p.posUpdate()
    p.frameUpdate()
    p.setHealth("none", 0)
    #zone loading handler
    if p.yPos >= 1000:
        w.zoneY -= 1
        w.doLoadZone = True
        p.yPos =w.worldTop + 10
    elif p.yPos <=0:
        w.zoneY += 1
        w.doLoadZone = True
        p.yPos = w.worldBottom - 10
    elif p.xPos >= 1000:
        w.zoneX += 1
        w.doLoadZone = True
        p.xPos = w.worldLeft + 10
    elif p.xPos <= 0:
        w.zoneX -=1
        w.doLoadZone = True
        p.xPos = w.worldRight - 10
    if w.doLoadZone == True:
        w.loadZone()
        #print("From Main:", objects,enemies,items)
        w.doLoadZone = False
    p.player()
    #p.hitbox()
    if p.hasSword == True:
        if keyboard.is_pressed("e") == True and p.attackCooldown < 5:
            p.isAttacking = True
            for en in enemies:
                enId = en.enemyId()
                didHit = p.attack(enId)
                if didHit == True:
                    en.health -=1
            p.attackCooldown += 1
        elif keyboard.is_pressed("e") == True and p.attackCooldown == 5:
            p.isAttacking = False
        elif keyboard.is_pressed("e") == False:
            p.attackCooldown = False
            p.isAttacking = False
    dig = p.dig()
    if dig == True:
        p.isDigging = True
    else:
        p.isDigging = False
                    #print(en.health)
    #print("x =", p.xPos)
    #print("y = ",p.yPos)
    #print("current slot:", p.currentHeartSlot)
    #print("hearts:", p.healthVal)

def updateItems(items):
    gameWindow.bkgrnd.delete("item", "itemHitbox")

    #print(items)
    #print(w.currentZoneItems)
    for i in items:
        #i.itemHitbox()
        i.itemImage()
        col.collision(i, p, w)
        #print("Updated Item with name:", i.name, "at", i.xPos, i.yPos)

def updateObjects(objects):
    gameWindow.bkgrnd.delete("object", "objectHitbox")
    for o in objects:
        o.objectHitbox()
        o.objectImage()
        col.collision(o, p, w)
        if o.name == "digSpot":
            if o.isDug == True:
                o.sprite = Graphics.digSpotDug
def updateConsole(enemies):
    gameWindow.bkgrnd.delete("consoleWindow", "consoleText")
    c.checkOn()
    if c.isOn == True:
        c.consoleInput()
        if c.gm == True:
            p.gm = True
        elif c.gm == False:
            p.gm = False
        if c.doAi == False:
            for i in enemies:
                if i.isDead == False:
                    i.doAi = False
        elif c.doAi == True:
            for i in enemies:
                if i.isDead == False:
                    i.doAi = True
        if c.changeZone == True:
            c.changeZone = False
            if c.zoneDim == "o":
                w.subZone = 0
            elif c.zoneDim == "c":
                w.subZone = 1
            w.zoneX = int(c.zoneX)
            w.zoneY = int(c.zoneY)
            c.zoneDim = ""
            c.zoneX = 0
            c.zoneY = 0
            w.loadZone()
        if c.giveSword == True:
            p.hasSword = True
            c.giveSword = False
        if c.giveShovel == True:
            p.hasShovel = True
            c.giveShovel = False
def updateInventory():
    gameWindow.bkgrnd.delete("itemInventory", "itemInventoryItem")
    if i.isOpen == True:
        i.itemInventoryHandler(p)
        i.checkOn()
    elif i.isOpen == False:
        i.checkOn()
def gameOver():
        gameWindow.bkgrnd.create_rectangle(0,0,1000,1000, fill = "black")
        gameWindow.bkgrnd.create_text(500,500, font = Graphics.gameOverFont, text = "Game Over!", fill = "red")

#Updates everything
def update():
    objects = w.currentZoneObjects
    items = w.currentZoneItems
    enemies = w.currentZoneEnemies
    #print("Updated")
    #if statements may appear to be redundant, but are there to pause the game when specific events are true
    if c.isOn == True:
        #print("Console active")
        updateConsole(enemies)
        #updateItems()
    else:
        if i.isOpen == True:
            updateInventory()
            updateConsole(enemies)
        else:
            updateInventory()
            updateConsole(enemies)
            updateObjects(objects)
            updateItems(items)
            updateEnemies(enemies, objects)
            updatePlayer(enemies)
            if p.isGameOver == True:
                gameOver()
    #print(p.hasSword)
    gameWindow.root.after(100, update)
gameWindow.bkgrnd.pack()

w.loadZone()
p.player()

gameWindow.root.after(100, update)
gameWindow.root.mainloop()
