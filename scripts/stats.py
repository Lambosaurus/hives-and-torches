import random

def roll(faces, count = 1):
    return sum(random.randint(1, faces) for i in range(count))

def clamp(v, low = None, high = None):
    if low != None and v < low: return low
    if high != None and v > high: return high
    return v

def fatigue(level, strength):
    strength = clamp(strength, 0)
    return 4 + roll(level, 4) + (strength * level)

# For some sample testing for fatigue at lvl 3
#print( [fatigue(3,1) for i in range(10)] )

