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
dungeondetailsconfidence=0.65
labenterconfidence=0.7
clickinterval = 1
useparty2 = True
runonce = False
instantbattle = True
imageDir = './Images/'
treasure = imageDir + 'Treasure.png'
exploration = imageDir + 'Exploration.png'
portal = imageDir + 'Portal.png'
master = imageDir + 'Master.png'
onslaught = imageDir + 'Onslaught.png'
restoration = imageDir + 'Restoration.png'
combatred = imageDir + 'combatred.png'
combatyellow = imageDir + 'combatyellow.png'
combatgreen = imageDir + 'combatgreen.png'
combatshiny = imageDir + 'CombatShiny.png'

#Set Priorities
p1 = treasure
p2 = exploration
p3 = combatred
p4 = onslaught
p5 = restoration
p6 = combatyellow
p7 = combatgreen
p8 = portal
p9 = master
pList = [p1,p2,p3,p4,p5,p6,p7,p8,p9]


#Painting clicks

class Painting:
    def __init__(self, paintinglocation,paintingtype,paintingimage):
        self.paintinglocation = paintinglocation #pyautogui box
        self.painginttype = paintingtype #string in treasure,exploration, combatantred, combatantyellow
                                            #, combatantgreen, onslaught, restoration, portal or master
        self.paintingimage = paintingimage #string with file location

class Button:
    def __init__(self, buttonlocation,buttontype,buttonimage,buttonconfidence):
        self.buttonlocation = buttonlocation #pyautogui box
        self.buttontype = buttontype #string in close, dungeondetails, enter, go, labenter
                                        #, moveone, next, ok, open, skip, usekey,yes
        self.buttonimage = buttonimage #string with file location
        self.buttonconfidence = buttonconfidence #float <= 1

def treasureclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickinterval)
    if debug2on: print('Treasure painting found')
    time.sleep(2)
    treasureclick2()
    return

def treasureclick2():
    while pag.locateOnScreen('./Images/TreasureLeft.png',confidence=treasureconfidence) is not None \
            or pag.locateOnScreen('./Images/TreasureMid.png',confidence=treasureconfidence) is not None \
            or pag.locateOnScreen('./Images/TreasureRight.png',confidence=treasureconfidence) is not None:
        if debug2on: print('Looking for closed treasure')
        time.sleep(2)
        if debug2on: print('Clicking on chest ')
        clicktreasure()
        if pag.locateOnScreen('./Images/UseKey.png',confidence=confidence) is not None:
            if debug2on: print('Need to use a key')
            clickusekey()
        if debug2on: print('Clicking open')
    time.sleep(1)
    clickmoveon()
    return


def explorationclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickinterval)
    if debug2on: print('Exploration painting found')
    time.sleep(2)
    if pag.locateOnScreen('./Images/MoveOn.png',confidence=confidence) is not None:
        if debug2on: print('Found Move On')
        clickmoveon()
        return
    if pag.locateOnScreen('./Images/Yes.png',confidence=confidence) is not None:
        if debug2on: print('Door found, clicking yes')
        clickyes()
    time.sleep(6)
    if pag.locateOnScreen('./Images/ChooseParty.png',confidence=dungeondetailsconfidence) is not None:
        if debug2on: print('It was a battle screen')
        battleclick2()
        return
    if pag.locateOnScreen('./Images/TreasureLeft.png',confidence=treasureconfidence) is not None:
        if debug2on: print('It was a treasure screen')
        treasureclick2()
        return


def battleclick(box):
    pag.click(pag.center(box),clicks=2,interval=clickinterval)
    if instantbattle:
        waitforinstantbattle()
        clickinstantbattle()
        waitforbeginbattle()
        clickbeginbattle()
        battleclick3()
        return
    waitforenter()
    if debug2on: print('Clicking Enter')
    clickenter()
    time.sleep(3)
    if debug2on: print('Starting battleclick2')
    battleclick2()
    return

def battleclick2():
    time.sleep(2)
    if debug2on: print('Looking for Choose Party screen')
    while pag.locateOnScreen('./Images/ChooseParty.png',confidence=dungeondetailsconfidence) is None:
        time.sleep(1)
    if useparty2:
        if debug2on and pag.locateOnScreen('./Images/DungeonDetails.png',confidence=dungeondetailsconfidence) is not None:
            print('Found Dungeon Details button')
        clickdungeondetails()
        party2 = False
        waitforclose()
        if pag.locateOnScreen('./Images/MagicPot.png',confidence=confidence) is not None:
            party2=True
        if debug2on:
            print('Using Lab Party 2: ' + str(party2))
        waitforclose()
        if debug2on and pag.locateOnScreen('./Images/Close.png',confidence=confidence) is not None:
            print('Found Close button')
        clickclose()
        time.sleep(3)
        if debug2on and party2:
            if pag.locateOnScreen('./Images/LabParty2.png',confidence=confidence) is not None:
                print('Clicking lab party 2')
            elif pag.locateOnScreen('./Images/LabParty2.png',confidence=confidence) is None:
                print('Could not find lab party 2 to click')
        if party2:
            clicklabparty2()
    if debug2on and pag.locateOnScreen('./Images/GO.png',confidence=confidence) is not None:
        print('Found the GO button')
    clickgo()
    time.sleep(2)
    if pag.locateOnScreen('./Images/OK.png',confidence=confidence) is not None:
        if debug2on: print('Found the OK button')
        clickok()
    battleclick3()
    return

def battleclick3():
    while pag.locateOnScreen('./Images/SKIP.png',confidence=confidence) is None:
        if debug2on: print('Waiting for combat to finish')
        time.sleep(2)
    if debug2on: print('Clicking skip')
    clickskip()
    while pag.locateOnScreen('./Images/Next.png',confidence=confidence) is None:
        time.sleep(1)
    if debug2on: print('Clicking Next')
    clicknext()
    waitforpaintings()
    return

def masterclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickinterval)
    if debug2on: print('Master painting found')
    waitforenter()
    #waitforinstantbattle()
    #clickinstantbattle()
    #waitforenter()
    #clickenter()
    if debug2on: print('Found the Enter button')
    clickenter()
    if debug2on: print('Starting battleclick2')
    battleclick2()
    if runonce:
        quit(1)
    return

def restonclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickinterval)
    if debug2on: print('Restoration or Onslaught painting found')
    waitformoveon()
    clickmoveon()
    waitforpaintings()
    return

def portalclick(box):
    pag.click(pag.center(box), clicks=2, interval=clickinterval)
    time.sleep(2)
    waitforok()
    clickok()
    waitforpaintings()
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
    pag.click(pag.locateOnScreen('./Images/Enter.png',confidence=labenterconfidence))
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
    if pag.locateOnScreen('./Images/TreasureLeft.png',confidence=treasureconfidence) is not None:
        pag.click(pag.locateOnScreen('./Images/TreasureLeft.png', confidence=treasureconfidence))
        return
    if pag.locateOnScreen('./Images/TreasureMid.png',confidence=treasureconfidence) is not None:
        pag.click(pag.locateOnScreen('./Images/TreasureMid.png', confidence=treasureconfidence))
        return
    if pag.locateOnScreen('./Images/TreasureRight.png',confidence=treasureconfidence) is not None:
        pag.click(pag.locateOnScreen('./Images/TreasureRight.png', confidence=treasureconfidence))
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

def clickinstantbattle():
    pag.click(pag.locateOnScreen('./Images/InstantBattle.png',confidence=confidence))
    return

def clickbeginbattle():
    pag.click(pag.locateOnScreen('./Images/BeginBattle.png',confidence=confidence))
    return

#Common waiting games
def waitforpaintings():
    while pag.locateOnScreen('./Images/ChoosePainting.png',confidence=confidence) is None \
            and pag.locateOnScreen('./Images/ChoosePaintingLastFloor.png',confidence=confidence) is None \
            and pag.locateOnScreen('./Images/Portal.png',confidence=confidence) is None \
            and pag.locateOnScreen('./Images/Master.png',confidence=confidence) is None:
        if debug2on:
            print('Waiting for paintings to come up again')
        if pag.locateOnScreen('./Images/Close.png',confidence=confidence) is not None:
            clickclose()
            time.sleep(1)
            if pag.locateOnScreen('./Images/Close.png', confidence=confidence) is not None:
                clickclose()
            break
        time.sleep(2)

def waitforclose():
    while pag.locateOnScreen('./Images/Close.png', confidence=confidence) is None:
        time.sleep(1)
    return

def waitforok():
    while pag.locateOnScreen('./Images/OK.png', confidence=confidence) is None:
        time.sleep(1)
    return

def waitforenter():
    while pag.locateOnScreen('./Images/Enter.png', confidence=labenterconfidence) is None:
        time.sleep(1)
    return

def waitformoveon():
    while pag.locateOnScreen('./Images/MoveOn.png', confidence=confidence) is None:
        time.sleep(1)
    return

def waitforinstantbattle():
    while pag.locateOnScreen('./Images/InstantBattle.png', confidence=confidence) is None:
        time.sleep(1)
    return

def waitforbeginbattle():
    while pag.locateOnScreen('./Images/BeginBattle.png', confidence=confidence) is None:
        time.sleep(1)
    return

#Starting Labs

def startlab():
    if debug3on and pag.locateOnScreen('./Images/OnLab.png',confidence=labenterconfidence) is not None:
        print('Found current labyrinth')
    pag.click(pag.locateOnScreen('./Images/OnLab.png', confidence=labenterconfidence))
    if debug3on and pag.locateOnScreen('./Images/LabEnter.png',confidence=confidence) is not None:
        print('Found Lab Enter')
    clicklabenter()
    waitforenter()
    if debug3on and pag.locateOnScreen('./Images/Enter.png',confidence=labenterconfidence) is not None:
        print('Found Enter')
    clickenter()
    time.sleep(2)
    if pag.locateOnScreen('./Images/OK.png',confidence=confidence) is not None:
        clickok()
    waitforok()
    clickok()
    return


def main():

    if debug1on: print('Starting Main')

    if pag.locateOnScreen('./Images/Lab3.png',confidence=labenterconfidence) \
            or pag.locateOnScreen('./Images/OnLab3.png',confidence=labenterconfidence):

        if debug1on: print('Starting Lab')

        startlab()


    priority = None

    #need to get the paintings priority on screen
    waitforpaintings()

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
    if priority == combatred or priority == combatyellow or priority == combatgreen:
        if debugon: print('Starting Combatant Painting')
        battleclick(pag.locateOnScreen(priority, confidence=confidence))
    if priority == master:
        if debugon: print('Starting Master Painting')
        masterclick(pag.locateOnScreen(priority,confidence=confidence))



    main()



if __name__ == "__main__":
    main()
