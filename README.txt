To run: 
open terminal/comand prompt
navigate to directory with "Main.py"
run "Main.py" with terminal/cmd prompt

For Mac Users:
make sure quartz is installed: pip3 install pyobjc (may need to run as admin/sudo)

Controls:
WASD to move
E to attack (after getting sword)
B to bring up inventory
` to bring up The Console
Once in console:
G to toggle God Mode (Invincibility)
A to toggle AI

Current features:
Enemy AI:
-Will charge at player if they can see him
-If not, they'll wander around aimlessly (but won't leave the zone)

Player:
-basic animations for moving and attacking
-basic attack ability

Collision:
-capable of seeing if any objects on the screen are overlapping (currently only called regarding Player)

World Gen:
-basic "new zone generator" (if the player walks to the edge of the screen, he will be placed on the opposite end and the misc details will regenerate)

The Console:
-Cheat terminal (purely for testing...)
-Detects user commands to stop/start various pieces of code being run

Notes:
-All created without using pygame or other Python game engine/API
-Made in Microsoft Visual Studio Code
