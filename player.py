# Max Level
LEVEL_MAX = 100

# Player Class
class Player(object):
    # Name will be a string containing the name of the player
    # Mode will be a string representing the difficulty level
    # Level will be an int between 1 - 100
    # Xp will be current xp needed for next level-up
    #       next level xp is calcualted by using this formula: f(x)=x^2 + 2*x

    def __init__(self, name, mode):     # Initialisation
        self.name = name
        self.mode = mode
        self.level = 0
        self.currentXp = 0
        self.nextLevelXp = self.get_next_level_xp(self.level + 1)
        self.currentTry = 0

    def __repr__(self):                 # Representation
        str = "<----- <[%s]> ----- Lvl <[%d]> ----- Xp <[%d / %d]> ----- Mode <[%s]> ----->" % \
                (self.name, self.level, self.currentXp, self.nextLevelXp, self.mode)
        return str

    def level_checkMax(self):
        if self.level >= LEVEL_MAX:
            return True
        else:
            return False

    # Get next level xp using the formula
    def get_next_level_xp(self, level):
        return (level * level) + (level * 2)

    def resetTries(self):
        self.currentTry = 0

    # Level up, clean xp, set next level xp
    def level_up(self):
        self.level += 1
        self.nextLevelXp = self.get_next_level_xp(self.level + 1)

    # Check if xp is sufficieint for next level
    def xp_sufficient(self):
        if(self.currentXp >= self.nextLevelXp):
            self.currentXp -= self.nextLevelXp
            return True
        else:
            return False


    # Add xp
    def xp_add(self, xp):
        self.currentXp += xp

    # Xp Manage
    def xp_manage(self, xp):
        self.xp_add(xp)
        while self.xp_sufficient():
            if not self.level_checkMax():
                self.level_up()
            else:
                return False

        return True
