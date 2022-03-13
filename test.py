consoleText = input()
zoneDim = ""
zoneX = 0
zoneY = 0


#Z, x, y; Z=zonedim
def setZone():
    zoneVarsStr = consoleText[:0] + consoleText[3:]
    zoneVarsRaw = zoneVarsStr.split(", ")
    zoneVars = []
    for i in zoneVarsRaw:
        try:
            zoneVars += int(i)
        except:
            zoneVars += i
    zoneDim = zoneVars[0]
    zoneX = zoneVars[1]
    zoneY = zoneVars[2]
setZone()
