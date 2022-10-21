from tokenize import String
import keyboard


class MODES:
    START = "START"
    MENU = "MENU"
    WORLD = "WOLRD"
    BATTLE = "BATTLE"
    TRADE = "TRADE"


class Interface(object):

    #prints a single line of texts to show keybindings


    def __init__(self):
        self.mode = MODES.START
        self.menuPosition = 7 #number of chars in the first menu items starts at
        self.startScreen = '''
|     >NEW GAME                                              |
|      CONTINUE                                              |
|      EXIT                                                  |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |'''
        self.log = ''
        

    def printHud(self):
              #remember the game screen is 60 characters long           v60v
              #123456789012345678901234567890123456789012345678901234567890
        print("| up:W  down:S  left:A  right:D  interact:E   menu/quit:ESC |")
        pass

    def addToLog(self, new):
        
        self.log += new
        pass

    def clearLog(self):
        self.log = '|'
        pass

    def printLog(self):
        
        print(self.log)
        
    def setModeStart(self):
        self.mode = MODES.START

    def setModeMenu(self):
        self.mode = MODES.MENU

    def setModeWorld(self):
        self.mode = MODES.WORLD

    def setModeBattle(self):
        self.mode = MODES.BATTLE
        self.menuPosition = 63#update this

    def setModeTrade(self):
        self.mode = MODES.TRADE

   
    def startMenu(self, input):

        constant = 63 #number of chars in the next menu item is
        screen = '''
|      NEW GAME                                              |
|      CONTINUE                                              |
|      EXIT                                                  |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |
|                                                            |'''

#7
        screenChars = list(screen)
        match input:
            case 'w':
                screenChars[self.menuPosition] = ' '
                self.menuPosition-=constant
                screenChars[self.menuPosition] = '>'
                print(''.join(screenChars))
            case 's':
                screenChars[self.menuPosition] = ' '
                self.menuPosition+=constant
                screenChars[self.menuPosition] = '>'
                print(''.join(screenChars))
            case 'e':
                if(screenChars[self.menuPosition+1] == "N"):
                    self.setModeWorld()
                    return "NEW"
                if(screenChars[self.menuPosition+1] == "C"):
                    self.setModeWorld()
                    #player populated in Run_game, not in here
                    return "CONTINUE"
                if(screenChars[self.menuPosition+1] == "E"):

                    return "STOP"

    def battle(self, player, filemon, input):
        #This function will be called upon interacting with a wild(or rather unowned) filemon
        screen = '''
|                                                            |
|    [playerMon         ]            [enemyMon          ]    |
|    (=========)                               (========)    |
|                                                            |
|                                                            |
|                                                            |
|   >Fight  Inventory                                        |
|    Info   Flee                                             |
|    [    Battle Log                                    ]    |'''
        #sys.stdout.write("test")
        #sys.stdout.flush()
        firstLine = '''
|                                                            |'''
        firstMon = player.filemons[0]
        playerMonName = firstMon.name
        enemyName = filemon.name

        if(len(playerMonName) > 19):
            ext = '.' + firstMon.type
            playerMonName = playerMonName[:(len(playerMonName) - len(ext))] + ext
        if(len(enemyName) > 19):
            ext = '.' + filemon.type
            enemyName = enemyName[:len(playerMonName) - len(ext)] + ext
        

        sumChars = len(playerMonName) + len(enemyName) + 4
        numSpaces = 50 - sumChars
        nameLine = '|    ' + '[' + playerMonName + ']' + (' ' * numSpaces) + ' '  + '[' +enemyName + ']' + '    |'
        print(nameLine)
        print('debug')
        return False #when finished return true
        

    #prints all information related to the mon in a readable format
    #this will basically be the go to method whenever a mon needs to be represented in game
    def printMon(self):

        pass


    def getKeyPress(self):
            press = keyboard.read_key()
            return press

    def printHud(self):
                  #remember the game screen is 60 characters long           v60v
                  #123456789012345678901234567890123456789012345678901234567890
            print("| up:W  down:S  left:A  right:D  interact:E   menu/quit:ESC |")
            pass


def getKeyPress():
    press = keyboard.read_key()
    return press

def printHud():
          #remember the game screen is 60 characters long           v60v
          #123456789012345678901234567890123456789012345678901234567890
    print("| up:W  down:S  left:A  right:D  interact:E   menu/quit:ESC |")




