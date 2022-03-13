from tkinter import *
import tkinter.font as tkFont
#don't know if I'll change this: all sprites except player are taken from LttP

class Graphics:
    gameOverFont = tkFont.Font(size = 30)
    consoleFont = tkFont.Font(size = 12)

    #creates images

    #Menus
    consoleWindow = PhotoImage(file = "Assets/console.png")

    itemInventory = PhotoImage(file = "Assets/inventoryItems.png")
    itemInventory = itemInventory.zoom(2,2)

    #Items
    shovel = PhotoImage(file = "Assets/shovel.png")
    shovel = shovel.zoom(3,3)

    sword1 = PhotoImage(file = "Assets/sword1.png")
    sword1 = sword1.zoom(3,3)

    sword1Down = PhotoImage(file = "Assets/sword1Down.png")
    sword1Down =sword1Down.zoom(4,5)

    sword1Up = PhotoImage(file = "Assets/sword1.png")
    sword1Up =sword1Up.zoom(4,5)

    sword1Left = PhotoImage(file = "Assets/sword1Left.png")
    sword1Left =sword1Left.zoom(4,5)

    sword1Right = PhotoImage(file = "Assets/sword1Right.png")
    sword1Right =sword1Right.zoom(4,5)

    heartPickup = PhotoImage(file = "Assets/heartPickup.png")

    #Player
    playerSpriteIdle = PhotoImage(file = "Assets/Player.png")
    playerSpriteIdle = playerSpriteIdle.zoom(3,3)

    playerSpriteWalkDown1 = PhotoImage(file = "Assets/PlayerWalk1.png")
    playerSpriteWalkDown1 = playerSpriteWalkDown1.zoom(3,3)

    playerSpriteWalkDown2 = PhotoImage(file = "Assets/PlayerWalk2.png")
    playerSpriteWalkDown2 = playerSpriteWalkDown2.zoom(3,3)

    playerSpriteIdleUp = PhotoImage(file = "Assets/PlayerUp.png")
    playerSpriteIdleUp = playerSpriteIdleUp.zoom(3,3)

    playerSpriteWalkUp1 = PhotoImage(file = "Assets/PlayerUp1.png")
    playerSpriteWalkUp1 = playerSpriteWalkUp1.zoom(3,3)

    playerSpriteWalkUp2 = PhotoImage(file = "Assets/PlayerUp2.png")
    playerSpriteWalkUp2 = playerSpriteWalkUp2.zoom(3,3)

    playerSpriteIdleRight = PhotoImage(file = "Assets/PlayerRight.png")
    playerSpriteIdleRight = playerSpriteIdleRight.zoom(3,3)

    playerSpriteWalkRight1 = PhotoImage(file = "Assets/PlayerRight1.png")
    playerSpriteWalkRight1 = playerSpriteWalkRight1.zoom(3,3)

    playerSpriteWalkRight2 = PhotoImage(file = "Assets/PlayerRight2.png")
    playerSpriteWalkRight2 = playerSpriteWalkRight2.zoom(3,3)

    playerSpriteIdleLeft = PhotoImage(file = "Assets/PlayerLeft.png")
    playerSpriteIdleLeft = playerSpriteIdleLeft.zoom(3,3)

    playerSpriteWalkLeft1 = PhotoImage(file = "Assets/PlayerLeft1.png")
    playerSpriteWalkLeft1 = playerSpriteWalkLeft1.zoom(3,3)

    playerSpriteWalkLeft2 = PhotoImage(file = "Assets/PlayerLeft2.png")
    playerSpriteWalkLeft2 = playerSpriteWalkLeft2.zoom(3,3)

    playerAttackDown = PhotoImage(file = "Assets/PlayerAttackDown.png")
    playerAttackDown = playerAttackDown.zoom(3,3)

    playerAttackUp = PhotoImage(file = "Assets/PlayerAttackUp.png")
    playerAttackUp = playerAttackUp.zoom(3,3)

    playerAttackLeft = PhotoImage(file = "Assets/PlayerAttackLeft.png")
    playerAttackLeft = playerAttackLeft.zoom(3,3)

    playerAttackRight = PhotoImage(file = "Assets/PlayerAttackRight.png")
    playerAttackRight = playerAttackRight.zoom(3,3)

    #terrain
    groundNorm = PhotoImage(file = "Assets/groundNorm.png")
    groundNorm = groundNorm.zoom(3,3)

    groundCave = PhotoImage(file = "Assets/groundCave.png")
    groundCave = groundCave.zoom(3,3)

    grass = PhotoImage(file = "Assets/grass.png")
    grass = grass.zoom(3,3)

    digSpot = PhotoImage(file = "Assets/digSpot.png")
    digSpot = digSpot.zoom(2,2)

    digSpotDug = PhotoImage(file = "Assets/digSpotDug.png")
    digSpotDug = digSpotDug.zoom(2,2)

    tree1 = PhotoImage(file = "Assets/tree1.png")
    tree1 = tree1.zoom(3,3)

    caveWallTop = PhotoImage(file = "Assets/caveWallTop.png")
    caveWallTop = caveWallTop.zoom(3,3)

    caveWallLeft = PhotoImage(file = "Assets/caveWallLeft.png")
    caveWallLeft = caveWallLeft.zoom(3,3)

    caveWallRight = PhotoImage(file = "Assets/caveWallRight.png")
    caveWallRight = caveWallRight.zoom(3,3)

    caveWallBottom = PhotoImage(file = "Assets/caveWallBottom.png")
    caveWallBottom = caveWallBottom.zoom(3,3)

    #enemies
    guard1Down = PhotoImage(file = "Assets/enemyGuard1Down.png")
    guard1Down = guard1Down.zoom(3,3)

    guard1LookLeft = PhotoImage(file = "Assets/enemyGuard1DownLookLeft.png")
    guard1LookLeft = guard1LookLeft.zoom(3,3)

    guard1LookRight = PhotoImage(file = "Assets/enemyGuard1DownLookRight.png")
    guard1LookRight = guard1LookRight.zoom(3,3)

    guard1Left = PhotoImage(file = "Assets/enemyGuard1Left.png")
    guard1Left = guard1Left.zoom(3,3)

    guard1Right = PhotoImage(file = "Assets/enemyGuard1Right.png")
    guard1Right = guard1Right.zoom(3,3)

    guard1Up = PhotoImage(file = "Assets/enemyGuard1Up.png")
    guard1Up = guard1Up.zoom(3,3)

    #hearts
    heartFull = PhotoImage(file = "Assets/heartFull.png")
    heartFull = heartFull.zoom(3,3)

    heartHalf = PhotoImage(file = "Assets/heartHalf.png")
    heartHalf = heartHalf.zoom(3,3)

    heartEmpty = PhotoImage(file = "Assets/heartEmpty.png")
    heartEmpty = heartEmpty.zoom(3,3)