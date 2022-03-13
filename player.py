import keyboard
from window import gameWindow
from graphics import Graphics
import enemy
import item


from tkinter import *
class Player:
    gm = False
    isGameOver = False
    #items
    hasSword = False
    hasShovel = False
    isDigging = False
    yPos = 500
    xPos = 500
    currentPlayerSprite = 0 # 0=downIdle, 1= down1, 2= down2, 3=up1, 4=up2,5=right1, 6=right2, 7=left1, 8=left2, 9=upIdle, 10 =leftIdle, 11=rightIdle, 12=attackDown, 13-attackUp, 14=attackLeft, 15=attackRight
    currentSwordSprite = 0 #0=not drawn, 1=sword1Down, 2=sword1Up, 3=sword1Left, 4=sword1Right
    playerSprite = Graphics.playerSpriteIdle
    swordSprite = Graphics.sword1
    moving = "not" #if the player is moving and which direction they're going
    facing = "down"
    #movement
    def posUpdate(self):
        if keyboard.is_pressed('a') == True and keyboard.is_pressed('w') == True:
            self.xPos -= 15
            self.yPos -= 15
            self.moving = "up"
            self.facing = "up"
        elif keyboard.is_pressed('w') == True and keyboard.is_pressed('d') == True:
            self.xPos += 15
            self.yPos -= 15
            self.moving = "up"
            self.facing = "up"
        elif keyboard.is_pressed('s') == True and keyboard.is_pressed('d') == True:
            self.xPos += 15
            self.yPos += 15
            self.moving = "down"
            self.facing = "down"
        elif keyboard.is_pressed('s') == True and keyboard.is_pressed('a') == True:
            self.xPos -= 15
            self.yPos += 15
            self.moving = "down"
            self.facing = "down"
        elif keyboard.is_pressed('a') == True:
            self.xPos -= 15
            #print(self.xPos)
            self.moving = "left"
            self.facing = "left"
        elif keyboard.is_pressed('d') == True:
            self.xPos += 15
            #print(self.xPos)
            self.moving = "right"
            self.facing = "right"
        elif keyboard.is_pressed('w') == True:
            self.yPos -= 15
            #print(self.yPos)
            self.moving = "up"
            self.facing = "up"
        elif keyboard.is_pressed('s') == True:
            self.yPos += 15
            #print(self.yPos)
            self.moving = "down"
            self.facing = "down"
        else:
            self.moving = "not"
        #print("yPos =",self.yPos)
        #return self.yPos

    def hitbox(self):
        gameWindow.bkgrnd.create_rectangle(self.xPos + 30, self.yPos + 40, self.xPos - 30, self.yPos - 40, tags = "playerHitbox")
    counter = 0 #for handling walking animations
    isAttacking = False
    attackCooldown = 0 #makes attack run only for a short while pressing e and not constantly
    def attack(self, enemyId):
        if self.attackCooldown == False:
            direction = self.facing
            if direction == "down":
                print("player attacked down")
                #swordSweep = gameWindow.bkgrnd.create_rectangle(self.xPos + 25, self.yPos, self.xPos - 25, self.yPos + 100, tags = "swordSweepBox")
                swordHits = gameWindow.bkgrnd.find_overlapping(self.xPos + 25, self.yPos, self.xPos - 25, self.yPos + 100)
            elif direction == "up":
                print("player attacked up")
                #swordSweep = gameWindow.bkgrnd.create_rectangle(self.xPos + 25, self.yPos, self.xPos - 25, self.yPos - 100, tags = "swordSweepBox")
                swordHits = gameWindow.bkgrnd.find_overlapping(self.xPos + 25, self.yPos, self.xPos - 25, self.yPos - 100)
            elif direction == "right":
                print("player attacked right")
                #swordSweep = gameWindow.bkgrnd.create_rectangle(self.xPos, self.yPos + 25, self.xPos + 100, self.yPos - 25, tags = "swordSweepBox")
                swordHits = gameWindow.bkgrnd.find_overlapping(self.xPos, self.yPos + 25, self.xPos + 100, self.yPos - 25)
            elif direction == "left":
                print("player attacked left")
                #swordSweep = gameWindow.bkgrnd.create_rectangle(self.xPos, self.yPos + 25, self.xPos - 100 - 25, self.yPos - 25, tags = "swordSweepBox")
                swordHits = gameWindow.bkgrnd.find_overlapping(self.xPos, self.yPos + 25, self.xPos - 100, self.yPos - 25)
            for i in swordHits:
                #print(enemyId)
                if i == enemyId:
                    #print("I hit you!")
                    return True
    def dig(self):
        if self.hasShovel == True:
            if keyboard.is_pressed('q') == True:
                return True
    def frameUpdate(self):
        if self.isAttacking == True:
            if self.facing == "up":
                self.currentPlayerSprite = 13
                self.currentSwordSprite = 2
            elif self.facing == "down":
                self.currentPlayerSprite = 12
                self.currentSwordSprite = 1
            elif self.facing == "left":
                self.currentPlayerSprite = 14
                self.currentSwordSprite = 3
                #print(self.currentSwordSprite)
            elif self.facing == "right":
                self.currentPlayerSprite = 15
                self.currentSwordSprite = 4
                #print(self.currentSwordSprite)
        elif self.moving == "down":
            if self.counter >= 0 and self.counter < 3:
                self.currentPlayerSprite = 1
                self.currentSwordSprite = 0
                self.counter += 1
            elif self.counter >= 3 and self.counter < 5:
                self.currentPlayerSprite = 2
                self.currentSwordSprite = 0
                self.counter += 1
            elif self.counter == 5:
                self.counter = 0
        elif self.moving == "up":
            if self.counter >= 0 and self.counter < 3:
                self.currentPlayerSprite = 3
                self.currentSwordSprite = 0
                self.counter += 1
            elif self.counter >= 3 and self.counter < 5:
                self.currentPlayerSprite = 4
                self.currentSwordSprite = 0
                self.counter += 1
            elif self.counter == 5:
                self.counter = 0
        elif self.moving == "left":
            if self.counter >= 0 and self.counter < 3:
                self.currentPlayerSprite = 7
                self.currentSwordSprite = 0
                self.counter += 1
            elif self.counter >= 3 and self.counter < 5:
                self.currentPlayerSprite = 8
                self.currentSwordSprite = 0
                self.counter += 1
            elif self.counter == 5:
                self.counter = 0
        elif self.moving == "right":
            if self.counter >= 0 and self.counter < 3:
                self.currentPlayerSprite = 5
                self.currentSwordSprite = 0
                self.counter += 1
            elif self.counter >= 3 and self.counter < 5:
                self.currentPlayerSprite = 6
                self.currentSwordSprite = 0
                self.counter += 1
            elif self.counter == 5:
                self.counter = 0
        elif self.moving == "not" and self.facing == "down":
            self.currentPlayerSprite = 0
            self.currentSwordSprite = 0
        elif self.moving =="not" and self.facing == "up":
            self.currentPlayerSprite = 9
            self.currentSwordSprite = 0
        elif self.moving =="not" and self.facing == "Left":
            self.currentPlayerSprite = 10
            self.currentSwordSprite = 0
        elif self.moving =="not" and self.facing == "Right":
            self.currentPlayerSprite = 11
            self.currentSwordSprite = 0
    #function that draws the player to the screen
    def player(self):
        #print(self.currentPlayerSprite)
        if self.currentPlayerSprite == 0:
            self.playerSprite = Graphics.playerSpriteIdle
        elif self.currentPlayerSprite == 1:
            self.playerSprite = Graphics.playerSpriteWalkDown1
        elif self.currentPlayerSprite == 2:
            self.playerSprite = Graphics.playerSpriteWalkDown2
        elif self.currentPlayerSprite == 3:
            self.playerSprite = Graphics.playerSpriteWalkUp1
        elif self.currentPlayerSprite == 4:
            self.playerSprite = Graphics.playerSpriteWalkUp2
        elif self.currentPlayerSprite == 5:
            self.playerSprite =Graphics.playerSpriteWalkRight1
        elif self.currentPlayerSprite == 6:
            self.playerSprite =Graphics.playerSpriteWalkRight2
        elif self.currentPlayerSprite == 7:
            self.playerSprite =Graphics.playerSpriteWalkLeft1
        elif self.currentPlayerSprite == 8:
            self.playerSprite =Graphics.playerSpriteWalkLeft2
        elif self.currentPlayerSprite == 9:
            self.playerSprite =Graphics.playerSpriteIdleUp
        elif self.currentPlayerSprite == 10:
            self.playerSprite =Graphics.playerSpriteIdleLeft
        elif self.currentPlayerSprite == 11:
            self.playerSprite =Graphics.playerSpriteIdleRight
        elif self.currentPlayerSprite == 12:
            self.playerSprite =Graphics.playerAttackDown
        elif self.currentPlayerSprite == 13:
            self.playerSprite =Graphics.playerAttackUp
        elif self.currentPlayerSprite == 14:
            self.playerSprite =Graphics.playerAttackLeft
        elif self.currentPlayerSprite == 15:
            self.playerSprite =Graphics.playerAttackRight

        if self.currentSwordSprite == 1:
            self.swordSprite = Graphics.sword1Down
            #print("using sword down")
        elif self.currentSwordSprite == 2:
            self.swordSprite = Graphics.sword1Up
           # print("using sword up")
        elif self.currentSwordSprite == 3:
            self.swordSprite = Graphics.sword1Left
          #  print("using sword left")
        elif self.currentSwordSprite == 4:
            self.swordSprite = Graphics.sword1Right
         #   print("using sword right")
        #print("Facing:", self.facing)
        if self.isAttacking == True:
            if self.facing == "up":
                gameWindow.bkgrnd.create_image(self.xPos-7, self.yPos-50,anchor = CENTER, image = self.swordSprite, tags = "playerSword")
                gameWindow.bkgrnd.create_image(self.xPos, self.yPos, anchor = CENTER, image = self.playerSprite, tags = "player")
            elif self.facing == "down":
                gameWindow.bkgrnd.create_image(self.xPos, self.yPos, anchor = CENTER, image = self.playerSprite, tags = "player")
                gameWindow.bkgrnd.create_image(self.xPos-7, self.yPos + 50,anchor = CENTER, image = self.swordSprite, tags = "playerSword")
            elif self.facing == "left":
                gameWindow.bkgrnd.create_image(self.xPos-50, self.yPos+4,anchor = CENTER, image = self.swordSprite, tags = "playerSword")
                gameWindow.bkgrnd.create_image(self.xPos, self.yPos, anchor = CENTER, image = self.playerSprite, tags = "player")

            elif self.facing == "right":
                gameWindow.bkgrnd.create_image(self.xPos+50, self.yPos+4,anchor = CENTER, image = self.swordSprite, tags = "playerSword")
                gameWindow.bkgrnd.create_image(self.xPos, self.yPos, anchor = CENTER, image = self.playerSprite, tags = "player")

        else:
            gameWindow.bkgrnd.create_image(self.xPos, self.yPos, anchor = CENTER, image = self.playerSprite, tags = "player")

    def playerId(self):
        playerIdRAW = gameWindow.bkgrnd.find_withtag("player")
        return playerIdRAW[0]


    gainHeart = False #used to trigger adding an extra heart to the life count (nyi)
    currentHeartSlot = 3
    maxHealthSlot = 3 #the maximum heart value
    healthVal = [1,1,1,1]
    heartPosition = [10,35,60,85] #x coords
    # action refers to whether being damaged or healed (none is if just drawing health), amt is how much being healed or damaged
    def setHealth(self, action, amt):
        if action == "damage":
            #print("ran damage")
            for i in self.healthVal:
                if self.healthVal[self.currentHeartSlot] == 1 or self.healthVal[self.currentHeartSlot] == .5 :
                    self.healthVal[self.currentHeartSlot] -= amt
                    break
                elif self.healthVal[self.currentHeartSlot] == 0:
                    self.currentHeartSlot -= 1
            self.currentHeartSlot = self.maxHealthSlot
        elif action == "heal":
            #print("ran heal")
            for i in self.healthVal:
                if self.healthVal[self.currentHeartSlot] == .5 :
                    self.healthVal[self.currentHeartSlot] += amt
                    #print("added heart to heart with .5")
                    break
                elif self.healthVal[self.currentHeartSlot] == 0 and self.healthVal[self.currentHeartSlot - 1] == 1:
                    self.healthVal[self.currentHeartSlot] += amt
                    #print("added heart to heart with 0")
                    break
                elif self.healthVal[self.currentHeartSlot] == 0 and (self.healthVal[self.currentHeartSlot - 1] != 1 or self.healthVal[self.currentHeartSlot - 1] != .5):
                    self.currentHeartSlot -= 1
            self.currentHeartSlot = self.maxHealthSlot
        for i in reversed(self.healthVal):
            if i == 1:
                gameWindow.bkgrnd.create_image(self.heartPosition[self.currentHeartSlot] ,10 , anchor = NW, image = Graphics.heartFull, tags = "heartFull")
            elif i == .5:
                gameWindow.bkgrnd.create_image(self.heartPosition[self.currentHeartSlot] ,10 , anchor = NW, image = Graphics.heartHalf, tags = "heartHalf")
            elif i == 0:
                gameWindow.bkgrnd.create_image(self.heartPosition[self.currentHeartSlot] ,10 , anchor = NW, image = Graphics.heartEmpty, tags = "heartEmpty")
            if self.healthVal[0] == 0:
                self.isGameOver = True
            self.currentHeartSlot -=1
        self.currentHeartSlot = self.maxHealthSlot

