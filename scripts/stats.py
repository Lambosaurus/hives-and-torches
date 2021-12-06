import random

def roll(faces, count = 1):
    return sum(random.randint(1, faces) for i in range(count))

def clamp(v, low = None, high = None):
    if low != None and v < low: return low
    if high != None and v > high: return high
    return v

class Character():
    def __init__(self, name, strength = 0, finesse = 0, intellect = 0, will = 0, max_wounds = 3):
        self.name = name
        self.clones = 0

        self.strength = strength
        self.finesse = finesse
        self.intellect = intellect
        self.will = will
        self.max_wounds = max_wounds

        self.level = 0
        self.max_fatigue = 4
        self.restore_all()
        self.set_level(1)
        self.set_armor(0)
 
        self.ai = lambda foes: random.choice(foes)

    def clone(self):
        self.clones += 1
        name = "{}#{}".format(self.name, self.clones)
        char = Character(name, self.strength, self.finesse, self.intellect, self.will, self.max_wounds)
        char.set_level(self.level)
        char.set_armor(*self.armor)
        char.set_weapon(self.weapon_die)
        char.set_ai(self.ai)
        return char

    def set_ai(self, ai):
        self.ai = ai
        return self

    def __str__(self):
        return "{} ({}/{})".format(self.name, self.fatigue, self.max_fatigue)

    def select_foe(self, foes):
        return self.ai(foes)

    # Returns the character to a healthy state
    def restore_all(self):
        self.fatigue = self.max_fatigue
        self.wounds = 0
        self.alive = True
        return self

    # Restores the given number of fatigue
    def restore_fatigue(self, amount):
        self.fatigue = clamp(self.fatigue + amount, 0, self.max_fatigue)

    # Cures the given number of wounds
    def restore_wounds(self, amount):
        self.wounds = clamp(self.wounds - amount, 0, self.max_wounds)

    # Sets the armor value for the character
    def set_armor(self, armor, heavy = False):
        self.armor = (armor, heavy)
        self.defence = armor
        if not heavy:
            self.defence += clamp(self.finesse, 0)
        return self

    # Does successive levelups until the character is at the specified level
    def set_level(self, level):
        while self.level < level:
            self.level_up()
        return self

    # Sets the weapon die for the character
    def set_weapon(self, die):
        self.weapon_die = die
        return self

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
        fatigue = roll(4) + clamp(self.strength, 0)
        self.max_fatigue += fatigue
        self.fatigue += fatigue

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
                if verbose: print("{} takes wound {}".format(str(self), self.wounds))
 
    # Returns True if the character is wounded
    def is_wounded(self):
        return self.wounds > 0

def fight_round(char, foes, verbose = False):
    if len(foes) == 0:
        return
    foe = char.select_foe(foes)
    char.attack(foe, verbose=verbose)
    if not foe.is_alive():
        foes.remove(foe)

def fight(party1, party2, suprise_round = None, verbose = False):


    if suprise_round == None:
        suprise_round = len(party1)
    
    for i in range(suprise_round):
        i += len(party1) - suprise_round
        fight_round(party1[i], party2, verbose=verbose)

    while len(party1) > 0 and len(party2) > 0:
        for char in party2:
            fight_round(char, party1, verbose=verbose)
        for char in party1:
            fight_round(char, party2, verbose=verbose)
            
def main():
    pc_level = 3
    fighter = Character("Fighter", strength=2, finesse=1).set_weapon(8).set_level(pc_level).set_armor(5,True)
    fighter.set_ai( lambda foes: foes[0] )
    rogue = Character("Rogue", strength=0, finesse=3).set_weapon(6).set_level(pc_level).set_armor(3)
    wizard = Character("Wizard") .set_weapon(4).set_level(pc_level).set_armor(1)

    party = [
        fighter,
        rogue,
        wizard,
    ]

    goblin = Character("Goblin", strength=1, finesse=2, max_wounds=1).set_weapon(6).set_level(1)
    hobgoblin = Character("Hobgoblin", strength=3, finesse=1, max_wounds=3).set_weapon(8).set_level(3)
    hobgoblin.set_ai( lambda foes: foes[0] )
    goblins = [hobgoblin.clone()] + [goblin.clone() for i in range(4)]

    fight(party, goblins, suprise_round=2, verbose=True)

if __name__ == "__main__":
    main()

# For some sample testing for fatigue at lvl 3
#print( [fatigue(3,1) for i in range(10)] )

