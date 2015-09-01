# -*- coding: utf-8 -*-
from game import *

inp_name = str(input("Ayyyee! Welcome to Guess My Number! Let me know your name: "))
print("Choose Difficulty:")
print("1. Easy              interval = [1 - 1e2(100)]")
print("2. Medium            interval = [1 - 1e3(1 000)]")
print("3. Hard              interval = [1 - 1e4(10 000)]")
print("4. Insane            interval = [1 - 1e5(100 000)]")
print("5. Get Me Outta This interval = [1 - 5e5(500 000)]")
inp_difficulty = int(input())

if inp_difficulty < 1 or inp_difficulty > 5:
    print("U hurt my feelings human :c")
    sys.exit(0)

# Create Game Here
game = Game(inp_name, str(inp_difficulty))

# Game Loop Begins Here
while not game.ended:
    game.updateMainMenuView()
    game.menu()
    mmp = int(game.inp())

    if mmp == 1:
        game.clear()

        if game.player.level_checkMax():
            print("You are already max level! You can quit and be proud!")
            s = str(input("Press [Enter] to continue..."))
            continue

        if game.firstLaunch == True:
            print("Try to Guess My Number! :>")
            game.firstLaunch = False
        else:
            print("Back to your #" + str(game.matchesPlayed + 1) + " match? Wish you good luck!")

         # Generate Random Number
         # Get input and check
         # Control Tries
        game.generate()
        while not game.matchEnded:
            if game.triesLeft():
                print("\nTries Left: %d" % (game.triesleft))
                print("Input your guess(1 - %d)" % (game.randLimit))
                usr_inp = int(game.inp())

                if game.respond(usr_inp):
                    s = str(input("Press [Enter] to continue..."))
                    game.matchEnded = True
                else:
                    game.addTry()
                    continue
            else:
                game.addMatch()
                print("Sorry out of tries! You get no XP! Try a new Match!")
                s = str(input("Press [Enter] to continue..."))
                game.matchEnded = True

        game.player.resetTries()
        game.matchEnded = False
    elif mmp == 2:
        continue
    elif mmp == 3:
        game.ended = True

game.updateMainMenuView()
game.bye()
