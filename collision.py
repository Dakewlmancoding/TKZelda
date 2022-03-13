import player
import enemy
import item
import worldObjects
from window import *

class Collision:

     def collision(self, collidee, collider, world): #collider (often the player) is the thing moving into the collidee
        stuffInColliderHitbox = gameWindow.bkgrnd.find_overlapping(collider.xPos + 30, collider.yPos + 40, collider.xPos - 30, collider.yPos - 40)
        collideeType = type(collidee)
        colliderType = type(collider)
        if collideeType == enemy.Enemy:
            collideeId = collidee.enemyId()
        elif collideeType == item.Item:
            collideeId = collidee.itemId()
        elif collideeType == worldObjects.WorldObjects:
            collideeId = collidee.objectId()
        for i in stuffInColliderHitbox:
            if (collideeType == enemy.Enemy) and (i == collideeId):
                #print("collision with enemy")
                #print(collidee.xPos)
                #print(collider.xPos)
                if collidee.xPos >= collider.xPos:
                    collider.xPos -= 20
                elif collidee.xPos <= collider.xPos:
                    collider.xPos +=20
                if collidee.yPos <= collider.yPos:
                    collider.yPos +=20
                elif collidee.yPos >= collider.yPos:
                    collider.yPos -=20
                if colliderType == player.Player:
                    #print("collider is player")
                    if collider.gm == True:
                        break
                    else:
                        collider.setHealth("damage", .5)
            elif (collideeType == item.Item) and (i == collideeId):
                if colliderType == player.Player:
                    if collidee.name == "sword1":
                        collider.hasSword = True
                        collidee.xPos = 1100
                        collidee.yPos = 1100
                        print("picked up sword")
                    if collidee.name == "heartPickup":
                        collidee.xPos = 1100
                        collidee.yPos = 1100
                        collider.setHealth("heal", .5)
                        print("picked up heart", collidee.itemNum)
                    if collidee.name == "shovel":
                        collider.hasShovel = True
                        collidee.xPos = 1100
                        collidee.yPos = 1100
                        print("picked up shovel")
            elif (collideeType == worldObjects.WorldObjects) and (i == collideeId):
                if collidee.name == "digSpot":
                    if collider.isDigging == True:
                        collidee.isDug = True
                    if collidee.isDug == True:
                        if collidee.type == "warper":
                            world.subZone = collidee.subZoneNum
                            world.zoneX = collidee.zoneNumX
                            world.zoneY = collidee.zoneNumY
                            world.doLoadZone = True
                            print("warping to: sub zone ", world.subZone, ", at ", world.zoneX, ",", world.zoneY)
                    #collider.inDigSpot = True
                else:
                    if collidee.xPos >= collider.xPos:
                        collider.xPos -= 20
                    elif collidee.xPos <= collider.xPos:
                        collider.xPos +=20
                    if collidee.yPos <= collider.yPos:
                        collider.yPos +=20
                    elif collidee.yPos >= collider.yPos:
                        collider.yPos -=20