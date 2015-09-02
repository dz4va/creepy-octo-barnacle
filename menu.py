# Imports
import sys
import platform
from random import randint      # Random Number Generator
from gameResources import emojis

class Menu(object):
    # Clear the console the cross platformish way
    def clear(self):
        if platform.os.name == "posix":
            platform.os.system("clear")
        elif platform.os.name == "nt":
            platform.os.system("cls")
        else:
            print("Sorry I couldn't clear the screen :c")
            print("\n" * 100)

    # Main Menu
    def menu(self):
        if self.firstLaunch:
            print("\n1. Start Game")
        else:
            print("\n1. Continue Game")
        print("2. Update the View")
        print("3. Change Difficulty")
        print("4. Quit Game")

    # Difficulty Menu
    def difficultyMenu(self):
        print("< ---- <[       Choose Difficulty      ]> ---- >")
        print("1. Easy          <[1 - 2e1(20)]> ")
        print("2. Normal        <[1 - 1e2(100)]>")
        print("3. MLG           <[1 - 1e3(1 000)]")
        print("4. Doge          <[1 - 1e4(10 000)]")
        print("5. Illuminati    <[1 - 1e5(100 000)]>")
        print("6. Chuck Norris  <[1 - 5e5(500 000)]>")

    def pleaseWait(self):
        print("Please Wait...")

    # Generate New Emoji and get the input
    def inp(self):
        n = randint(1,len(emojis))
        st = "(" + emojis[str(n)] + ")> "
        return input(st)
