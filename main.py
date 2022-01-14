import time
import pyautogui as pag

#Debugging
debugon = True
debug1on = True #Debugging for Main
debug2on = True #Debugging for paintings
debug3on = True #Debugging for button clicks

#Global Variables
confidence = 0.9
treasureConfidence = 0.8
dungeondetailsconfidence=0.7
labenterconfidence=0.7
clickInterval = 1
imageDir = './Images/'
treasure = imageDir + 'Treasure.png'
exploration = imageDir + 'Exploration.png'
portal = imageDir + 'Portal.png'
master = imageDir + 'Master.png'
onslaught = imageDir + 'Onslaught.png'
restoration = imageDir + 'Restoration.png'
combatRed = imageDir + 'CombatRed.png'
combatYellow = imageDir + 'CombatYellow.png'
combatGreen = imageDir + 'CombatGreen.png'

#Set Priorities
p1 = treasure
p2 = exploration
p3 = portal
p4 = master
p5 = onslaught
p6 = restoration
p7 = combatRed
p8 = combatYellow
p9 = combatGreen
pList = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

#init variables
party2 = False
priority = None

#Painting clicks

def treasureclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickInterval)
    treasureclick2()
    return

def treasureclick2():
    while pag.locateOnScreen('./Images/TreasureChest.png',confidence=treasureConfidence) is not None:
        time.sleep(2)
        clicktreasure()
        if pag.locateOnScreen('./Images/UseKey.png',confidence=confidence) is not None:
            clickusekey()
        clickopen()
    clickmoveon()
    return


def explorationclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickInterval)
    time.sleep(10)
    if pag.locateOnScreen('./Images/MoveOn.png',confidence=confidence) is not None:
        clickmoveon()
        return
    if pag.locateOnScreen('./Images/Enter.png',confidence=confidence) is not None:
        clickenter()
        return
    if pag.locateOnScreen('./Images/DungeonDetails.png',confidence=confidence) is not None:
        battleclick2()
        return
    if pag.locateOnScreen('./Images/Treasure.png',confidence=confidence) is not None:
        treasureclick2()
        return


def battleclick(box):
    pag.click(pag.center(box),clicks=2,interval=clickInterval)
    clickenter()
    battleclick2()
    return

def battleclick2():
    clickdungeondetails()
    party2 = False
    if pag.locateOnScreen('./Images/MagicPot.png',confidence=confidence) is not None:
        party2=True
    clickclose()
    if party2:
        clicklabparty2()
    clickgo()
    time.sleep(2)
    if pag.locateOnScreen('./Images/OK.png') is not None:
        clickok()
    while pag.locateOnScreen('./Images/Skip.png',confidence=confidence) is None:
        time.sleep(2)
    clickskip()
    clicknext()
    #Master painting handling needs a close here
    while pag.locateOnScreen('./Images/Frame.png') is None:
        time.sleep(2)
    return

def masterclick(box):
    pag.click(pag.center(box), clicks=2, interval=0.5)
    time.sleep(3)
    clickenter()
    time.sleep(3)
    battleclick2()
    return

def restonclick(box):
    pag.click(pag.center(box), clicks=2, interval=0.5)
    clickmoveon()
    return

def portalclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickInterval)
    time.sleep(2)
    clickok()
    while pag.locateOnScreen('./Images/Frame.png',confidence=confidence) is None:
        time.sleep(2)
    return

#Button clicks

def clicknext():
    pag.click(pag.locateOnScreen('./Images/Next.png',confidence=confidence))
    return

def clickskip():
    pag.click(pag.locateOnScreen('./Images/SKIP.png',confidence=confidence))
    return

def clickmoveon():
    pag.click(pag.locateOnScreen('./Images/MoveOn.png',confidence=confidence))
    return

def clickgo():
    pag.click(pag.locateOnScreen('./Images/GO.png',confidence=confidence))
    return

def clickenter():
    pag.click(pag.locateOnScreen('./Images/Enter.png',confidence=confidence))
    return

def clicklabenter():
    pag.click(pag.locateOnScreen('./Images/LabEnter.png',confidence=confidence))
    return

def clickdungeondetails():
    pag.click(pag.locateOnScreen('./Images/DungeonDetails.png',confidence=dungeondetailsconfidence))
    return

def clickclose():
    pag.click(pag.locateOnScreen('./Images/Close.png',confidence=confidence))
    return

def clicklabparty2():
    pag.click(pag.locateOnScreen('./Images/LabParty2.png',confidence=confidence))
    return

def clickok():
    pag.click(pag.locateOnScreen('./Images/OK.png',confidence=confidence))
    return

def clicktreasure():
    pag.click(pag.locateOnScreen('./Images/Treasure.png',confidence=confidence))
    return

def clickusekey():
    pag.click(pag.locateOnScreen('./Images/UseKey.png',confidence=confidence))
    return

def clickopen():
    pag.click(pag.locateOnScreen('./Images/Open.png',confidence=confidence))
    return

#Starting Labs

def startlab():

    if debug3on and pag.locateOnScreen('./Images/Lab3.png',confidence=labenterconfidence) is not None:
        print('Found Lab3')
    pag.click(pag.locateOnScreen('./Images/Lab3.png',confidence=labenterconfidence))
    time.sleep(2)
    if debug3on and pag.locateOnScreen('./Images/LabEnter.png',confidence=confidence) is not None:
        print('Found Lab Enter')
    pag.click(pag.locateOnScreen('./Images/LabEnter.png',confidence=confidence))
    time.sleep(2)
    if debug3on and pag.locateOnScreen('./Images/Enter.png',confidence=confidence) is not None:
        print('Found Enter')
    pag.click(pag.locateOnScreen('./Images/Enter.png',confidence=confidence))
    time.sleep(2)
    while pag.locateOnScreen('./Images/OK.png',confidence=confidence) is not None:
        clickok()
    return


def main():
    if debug1on: print('Starting Main')
    if pag.locateOnScreen('./Images/Lab3.png',confidence=labenterconfidence):
        if debug1on: print('Starting Lab3')
        startlab()

    priority = None

    #need to get the paintings priority on screen
    pIndex=1
    for pIndex in pList:
        if pag.locateOnScreen(pIndex,confidence=confidence) is not None:
            if debugon: print('Found ' + pIndex)
            priority = pIndex
            if debugon: print('Priority set to ' + priority)
        if priority is not None:
            break

    if priority == treasure:
        if debugon: print('Starting Treasure Painting')
        raise Exception('Treasure picture is not taken yet')
        treasureclick(pag.locateOnScreen(priority, confidence=confidence))
    if priority == exploration:
        if debugon: print('Starting Exploration Painting')
        explorationclick(pag.locateOnScreen(priority, confidence=confidence))
    if priority == portal:
        if debugon: print('Starting Portal Painting')
        portalclick(pag.locateOnScreen(priority, confidence=confidence))
    if priority == onslaught or priority == restoration:
        if debugon: print('Starting Onslaught of Restoration Painting')
        restonclick(pag.locateOnScreen(priority, confidence=confidence))
    if priority == combatRed or priority == combatYellow or priority == combatGreen:
        if debugon: print('Starting Combatant Painting')
        treasureclick(pag.locateOnScreen(priority, confidence=confidence))
    if priority == master:
        if debugon: print('Starting Master Painting')
        masterclick(pag.locateOnScreen(priority,confidence=confidence))



    main()



if __name__ == "__main__":
    main()
