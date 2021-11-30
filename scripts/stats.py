from random import randint as r

# d(1,4) == d(4)
def d(n, m = None):
    if m == None: return r(1,n)
    return sum( r(1,m) for i in range(n) )

def clamp(v, low = None, high = None):
    if low != None and v < low: return low
    if high != None and v > high: return high
    return v

def fatigue(level, strength):
    strength = clamp(strength, 0)
    return 4 + d(level, 4) + (strength * level)


# For some sample testing for fatigue at lvl 3
#print( [fatigue(3,1) for i in range(10)] )

