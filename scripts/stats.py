import random

def roll(faces, count = 1):
    return sum(random.randint(1, faces) for i in range(count))

def clamp(v, low = None, high = None):
    if low != None and v < low: return low
    if high != None and v > high: return high
    return v

class Character():
    def __init__(self, name, strength = 0, finesse = 0, intellect = 0, will = 0, max_wounds = 1):
        self.name = name

        self.strength = strength
        self.finesse = finesse
        self.intellect = intellect
        self.will = will
        self.max_wounds = max_wounds

        self.level = 0
        self.max_fatigue = 4
        self.level_to(1)
        self.set_armor(0)
        self.restore_all()

    def __str__(self):
        return "{} ({}/{})".format(self.name, self.fatigue, self.max_fatigue)

    # Returns the character to a healthy state
    def restore_all(self):
        self.fatigue = self.max_fatigue
        self.wounds = 0
        self.alive = True

    # Restores the given number of fatigue
    def restore_fatigue(self, amount):
        self.fatigue = clamp(self.fatigue + amount, 0, self.max_fatigue)

    # Cures the given number of wounds
    def restore_wounds(self, amount):
        self.wounds = clamp(self.wounds - amount, 0, self.max_wounds)

    # Sets the armor value for the character
    def set_armor(self, armor):
        self.defence = self.finesse + armor

    # Does successive levelups until the character is at the specified level
    def level_to(self, level):
        while self.level < level:
            self.level_up()

    # Sets the weapon die for the character
    def set_weapon(self, die):
        self.weapon_die = die

    # Rolls the attacks for the character
    # If a foe is specified, the damage will be applied to the foe
    def attack(self, foe = None, verbose = False):
        damage = roll(self.weapon_die, 2) + self.strength
        if foe != None:
            if verbose: print("{} rolls an attack of {} against {}".format(str(self), damage, str(foe)))
            foe.damage(damage, verbose=verbose)
        return damage

    def announce(self):
        print("{}, level {}, {}/{} fatigue, {}/{} wounds".format(str(self), self.level, self.fatigue, self.max_fatigue, self.wounds, self.max_wounds))
        print("Str: {}, Fin: {}, Int: {}, Will: {}, Attack: 2d{}, Defence: {}".format(self.strength, self.finesse, self.intellect, self.will, self.weapon_die, self.defence))
    
    # Performs a level up
    def level_up(self):
        self.level += 1
        self.max_fatigue += roll(4) + clamp(self.strength, 0)

    # Returns true if the character is alive
    def is_alive(self):
        return self.alive

    # Returns true if the damage was a hit
    def damage(self, amount, verbose = False):
        amount -= self.defence
        amount = clamp(amount, 0)
        
        if amount > self.fatigue:
            self.fatigue = 0
            self.wound(verbose=verbose)
        else:
            if verbose: print("{} takes {} damage".format(str(self), amount))
            self.fatigue -= amount

        return amount > 0

    # Kills the character
    def kill(self, verbose = False):
        if verbose: print("{} is killed".format(str(self)))
        self.alive = False
    
    # Deals a wound to the character
    def wound(self, verbose = False):
        if self.wounds < self.max_wounds:
            self.wounds += 1

            if self.wounds >= self.max_wounds:
                self.kill(verbose=verbose)
            else:
                if verbose: print("{} is wounded".format(str(self)))
 
    # Returns True if the character is wounded
    def is_wounded(self):
        return self.wounds > 0


def pit_fight(char1, char2, verbose = False):
    while char1.is_alive() and char2.is_alive():
        char1.attack(char2, verbose=verbose)
        if char2.is_alive():
            char2.attack(char1, verbose=verbose)

def main():

    char1 = Character("Player", strength=0, finesse=2, max_wounds=3)
    char1.set_weapon(6)
    char1.level_to(1)
    char1.set_armor(1)
    char2 = Character("Goblin", strength=1, finesse=2)
    char2.set_weapon(6)
    char2.level_to(1)

    pit_fight(char1, char2, verbose=True)

if __name__ == "__main__":
    main()

# For some sample testing for fatigue at lvl 3
#print( [fatigue(3,1) for i in range(10)] )

