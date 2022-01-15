import time
import pyautogui as pag

#Debugging
debugon = True
debug1on = True #Debugging for Main
debug2on = True #Debugging for paintings
debug3on = True #Debugging for button clicks

#Global Variables
pag.PAUSE = 2.5
confidence = 0.9
treasureconfidence = 0.8
dungeondetailsconfidence=0.7
labenterconfidence=0.7
clickinterval = 1
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
p3 = combatRed
p4 = onslaught
p5 = restoration
p6 = portal
p7 = master
p8 = combatYellow
p9 = combatGreen
pList = [p1,p2,p3,p4,p5,p6,p7,p8,p9]


#Painting clicks

def treasureclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickinterval)
    if debug2on: print('Treasure painting found')
    time.sleep(2)
    treasureclick2()
    return

def treasureclick2():
    while pag.locateOnScreen('./Images/TreasureChest.png',confidence=treasureconfidence) is not None:
        if debug2on: print('Looking for closed treasure')
        time.sleep(2)
        if debug2on: print('Clicking on chest ')
        clicktreasure()
        if pag.locateOnScreen('./Images/UseKey.png',confidence=confidence) is not None:
            if debug2on: print('Need to use a key')
            clickusekey()
        if debug2on: print('Clicking open')
        while pag.locateOnScreen('./Images/Open.png',confidence=confidence) is None:
            time.sleep(2)
        clickopen()
    if debug2on: print('Moving on')
    time.sleep(1)
    clickmoveon()
    return


def explorationclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickinterval)
    if debug2on: print('Exploratiopn painting found')
    time.sleep(2)
    if pag.locateOnScreen('./Images/MoveOn.png',confidence=confidence) is not None:
        if debug2on: print('Found Move On')
        clickmoveon()
        return
    if pag.locateOnScreen('./Images/Yes.png',confidence=confidence) is not None:
        if debug2on: print('Door found, clicking yes')
        clickyes()
        time.sleep(6)
    if pag.locateOnScreen('./Images/DungeonDetails.png',confidence=dungeondetailsconfidence) is not None:
        if debug2on: print('It was a battle screen')
        battleclick2()
        return
    if pag.locateOnScreen('./Images/Treasure.png',confidence=confidence) is not None:
        if debug2on: print('It was a treasure screen')
        treasureclick2()
        return


def battleclick(box):
    pag.click(pag.center(box),clicks=2,interval=clickinterval)
    while pag.locateOnScreen('./Images/Enter.png',confidence=confidence) is None:
        time.sleep(1)
    if debug2on: print('Clicking Enter')
    clickenter()
    time.sleep(3)
    if debug2on: print('Starting battleclick2')
    battleclick2()
    return

def battleclick2():
    time.sleep(2)
    while pag.locateOnScreen('./Images/DungeonDetails.png',confidence=confidence):
        time.sleep(1)
    clickdungeondetails()
    party2 = False
    time.sleep(1)
    if pag.locateOnScreen('./Images/MagicPot.png',confidence=confidence) is not None:
        party2=True
    while pag.locateOnScreen('./Images/Close.png',confidence=confidence) is None:
        time.sleep(1)
    clickclose()
    while pag.locateOnScreen('./Images/LabParty2.png',confidence=confidence) is None:
        time.sleep(1)
    if party2:
        clicklabparty2()
    clickgo()
    time.sleep(2)
    if pag.locateOnScreen('./Images/OK.png',confidence=confidence) is not None:
        clickok()
    while pag.locateOnScreen('./Images/SKIP.png',confidence=confidence) is None:
        if debug2on: print('Waiting for combat to finish')
        time.sleep(2)
    if debug2on: print('Clicking skip')
    clickskip()
    while pag.locateOnScreen('./Images/Next.png',confidence=confidence) is None:
        time.sleep(1)
    if debug2on: print('Clicking Next')
    clicknext()
    #Master painting handling needs a close here
    while pag.locateOnScreen('./Images/Frame.png',confidence=confidence) is None or pag.locateOnScreen('./Images/PortalFrame.png',confidence=confidence):
        if debug2on: print('Waiting for paintings to come up again')
        if pag.locateOnScreen('./Images/Close.png',confidence=confidence) is not None:
            clickclose()
            time.sleep(1)
            if pag.locateOnScreen('./Images/Close.png', confidence=confidence) is not None:
                clickclose()
            break
        time.sleep(2)
    return

def masterclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickinterval)
    time.sleep(3)
    clickenter()
    time.sleep(3)
    battleclick2()
    return

def restonclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickinterval)
    clickmoveon()
    return

def portalclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickinterval)
    time.sleep(2)
    clickok()
    while pag.locateOnScreen('./Images/Frame.png',confidence=confidence) is None:
        time.sleep(2)
    time.sleep(2 )
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
    pag.click(pag.locateOnScreen('./Images/Treasure.png',confidence=treasureconfidence))
    return

def clickusekey():
    pag.click(pag.locateOnScreen('./Images/UseKey.png',confidence=confidence))
    return

def clickopen():
    pag.click(pag.locateOnScreen('./Images/Open.png',confidence=confidence))
    return

def clickyes():
    pag.click(pag.locateOnScreen('./Images/Yes.png',confidence=confidence))
    return

#Starting Labs

def startlab():

    if debug3on and pag.locateOnScreen('./Images/Lab3.png',confidence=labenterconfidence) is not None:
        print('Found Lab3')
    pag.click(pag.locateOnScreen('./Images/Lab3.png', confidence=labenterconfidence))
    pag.click(pag.locateOnScreen('./Images/OnLab3.png', confidence=labenterconfidence))
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
    if pag.locateOnScreen('./Images/Lab3.png',confidence=labenterconfidence) or pag.locateOnScreen('./Images/OnLab3.png',confidence=labenterconfidence):
        if debug1on: print('Starting Lab3')
        startlab()

    priority = None

    #need to get the paintings priority on screen
    pIndex=1
    for pIndex in pList:
        try:
            if pag.locateOnScreen(pIndex,confidence=confidence) is not None:
                if debugon: print('Found ' + pIndex)
                priority = pIndex
                if debugon: print('Priority set to ' + priority)
            if priority is not None:
                break
        except IOError:
            print('Paint image ' + pIndex + ' cannot be found')
            continue



    if priority == treasure:
        if debugon: print('Starting Treasure Painting')
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
        battleclick(pag.locateOnScreen(priority, confidence=confidence))
    if priority == master:
        if debugon: print('Starting Master Painting')
        masterclick(pag.locateOnScreen(priority,confidence=confidence))



    main()



if __name__ == "__main__":
    main()
