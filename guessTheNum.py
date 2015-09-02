# -*- coding: utf-8 -*-

import game

# Create gameInstance
gameInstance = game.Game()
gameInstance.clear()
print("< ---- <[ Welcome to Guess The Number! ]> ---- >")
print("< ---- <[    Input Your name Please    ]> ---- >")
inp_name = str(gameInstance.inp())
print("\n< ---- <[         So Charming!         ]> ---- >")
gameInstance.pleaseWait()
game.time.sleep(game.DEF_WAIT_TIME)

gameInstance.clear()
gameInstance.difficultyMenu()
inp_difficulty = int(gameInstance.inp())
while (inp_difficulty < 1 or inp_difficulty > 6):
    gameInstance.clear()
    print("You too Brutus?")
    game.time.sleep(game.DEF_WAIT_TIME)
    gameInstance.clear()
    gameInstance.difficultyMenu()
    inp_difficulty = int(gameInstance.inp())
else:
    gameInstance.clear()
    if inp_difficulty >= 3:
        print("Are you sure you are that pro?")
    else:
        print("You can't do more than that?")
    gameInstance.pleaseWait()
    game.time.sleep(game.DEF_WAIT_TIME)    


# Create Player here
gameInstance.createPlayer(inp_name, str(inp_difficulty))

# gameInstance Loop Begins Here
while not gameInstance.ended:
    gameInstance.updateMainMenuView()
    gameInstance.menu()
    mmp = int(gameInstance.inp())

    if mmp == 1:
        gameInstance.clear()

        if gameInstance.player.level_checkMax():
            print("You are already max level! You can quit and be proud!")
            s = str(input("Press [Enter] to continue..."))
            continue

        if gameInstance.firstLaunch == True:
            print("Try to Guess My Number! :>")
            gameInstance.firstLaunch = False
        else:
            print("Back to your #" + str(gameInstance.matchesPlayed + 1) + " match? Wish you good luck!")

         # Generate Random Number
         # Get input and check
         # Control Tries
        gameInstance.generate()
        while not gameInstance.matchEnded:
            if gameInstance.triesLeft():
                print("\nTries Left: %d" % (gameInstance.triesleft))
                print("Input your guess(1 - %d)" % (gameInstance.randLimit))
                usr_inp = int(gameInstance.inp())

                if gameInstance.respond(usr_inp):
                    s = str(input("Press [Enter] to continue..."))
                    gameInstance.matchEnded = True
                else:
                    gameInstance.addTry()
                    continue
            else:
                gameInstance.addMatch()
                print("Sorry out of tries! You get no XP! Try a new Match!")
                s = str(input("Press [Enter] to continue..."))
                gameInstance.matchEnded = True

        gameInstance.player.resetTries()
        gameInstance.matchEnded = False
    elif mmp == 2:
        continue
    elif mmp == 3:
        gameInstance.clear()
        gameInstance.difficultyMenu()
        inp_difficulty = int(gameInstance.inp())
        while (inp_difficulty < 1 or inp_difficulty > 6):
            gameInstance.clear()
            gameInstance.difficultyMenu()
            inp_difficulty = int(gameInstance.inp())
        else:
            gameInstance.clear()
            gameInstance.changeMode(str(inp_difficulty))
            print("Mode changed to: %s" % (gameInstance.player.mode))
            gameInstance.pleaseWait()
            game.time.sleep(game.DEF_WAIT_TIME)
    elif mmp == 4:
        gameInstance.ended = True

gameInstance.updateMainMenuView()
gameInstance.bye()
