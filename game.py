# Imports
from math import floor          # Floor the goddamn time

# Sys management
import time

# Game Stuff
from player import *
from gameResources import game_difficulty
from menu import *

# Move everything here jeeeeeez make the goddam code as clean as possible

# CONSTANTS
DEF_WAIT_TIME = 3

class Game(Menu):
    matchesPlayed = 0   # Match Counter
    sessionH = 0        # Session Hours
    sessionM = 0        # Session Minutes
    sessionS = 0        # Session Seconds
    ended = False       # Game State Indicator & While Loop Controller
    finishTime = 0      # Game finish time
    matchEnded = False  # Actual Match Controller

    # Construct the object dammit
    def __init__(self):
        #self.player = Player(name, mode)
        self.launchTime = time.time()
        self.randomNum = 0
        #self.gameTries = game_difficulty[mode]["tries"]
        #self.gameXp = game_difficulty[mode]["xp"]
        #self.randLimit = game_difficulty[mode]["limit"]
        self.triesleft = 0
        self.firstLaunch = True

    # Create Player Separately
    def createPlayer(self, name, mode):
        self.player = Player(name, mode)
        self.modeName = game_difficulty[mode]["name"]
        self.gameTries = game_difficulty[mode]["tries"]
        self.gameXp = game_difficulty[mode]["xp"]
        self.randLimit = game_difficulty[mode]["limit"]

    # Change mode/difficulty
    def changeMode(self, mode):
        self.player.mode = mode
        self.modeName = game_difficulty[mode]["name"]
        self.gameTries = game_difficulty[mode]["tries"]
        self.gameXp = game_difficulty[mode]["xp"]
        self.randLimit = game_difficulty[mode]["limit"]


    # How the game class is being represented
    def __repr__(self):
        self.calculateTimeDelta()
        st = "%s \n\nMax Tries: %d\nMatches Played: %d\nDifficulty: %s\nRandom Number Limit: %d\n%s" % \
            (str(self.player), self.gameTries, self.matchesPlayed, self.modeName, self.randLimit, self.time())
        return st

    # Add Match
    def addMatch(self):
        self.matchesPlayed += 1

    # Generate random number between lower and upper and set the randomNum
    def generate(self):
        self.randomNum = randint(1, self.randLimit)

    # Dammit Respond or level up and take shiet here
    def respond(self, inp_num):
        if inp_num == self.randomNum:
            self.addMatch()
            xp = randint(self.gameXp[self.player.currentTry - 1]["min"],self.gameXp[self.player.currentTry - 1]["max"])
            st = "< ---- You Win in %d tries! <[+%d]> XP added!" % \
                (self.player.currentTry + 1, xp)
            if self.player.xp_manage(xp):
                print(st)
            else:
                print("You have maxed out the level! Good Job! Spectacular! Amazing!")
                print("I would give you an achievement for that if I had one!")
                print("You should be proud " + self.player.name + "!")
            return True
        elif inp_num < self.randomNum:
            print("< ---- <[ Lo ]> ---- >")
        elif inp_num > self.randomNum:
            print("< ---- <[ Hi ]> ---- >")
        else:
            print("I didn't expect that!")
            return True

        return False

    # Menu Methods
    def clear(self):
        super(Game, self).clear()

    def menu(self):
        super(Game, self).menu()

    def inp(self):
        return super(Game, self).inp()

    def difficultyMenu(self):
        return super(Game, self).difficultyMenu()

    def pleaseWait(self):
        super(Game, self).pleaseWait()

    # Let meah See if da tries left
    def triesLeft(self):
        if self.player.currentTry < self.gameTries:
            self.triesleft = self.gameTries - self.player.currentTry
            return True
        else:
            return False

    # Tries++
    def addTry(self):
        self.player.currentTry = self.player.currentTry + 1

    # Update the console screen and game main menu
    def updateMainMenuView(self):
        self.clear()
        print(str(self))

    # Return Time String
    def time(self):
        st = "You have been playing for: %02d:%02d:%02d" % \
            (self.sessionH, self.sessionM, self.sessionS)
        return st
    # Calculate and set time delta
    def calculateTimeDelta(self):
        self.finishTime = time.time()
        differenceInSec = self.finishTime - self.launchTime

        # Set Time
        self.sessionM, self.sessionS = divmod(floor(differenceInSec), 60)
        self.sessionH, self.sessionM = divmod(floor(self.sessionM), 60)

    # Bye bye Noob, Haha!
    def bye(self):
        print("\nSee ya later :>")
