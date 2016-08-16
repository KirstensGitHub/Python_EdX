# python 2
#
# Homework 4, Problem 1
# "Lights On!"
#
# Name: Kirsten Ziman
#
#

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.


def mutate(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = 1 + oldL[i]
    return new_ith_element


def evolve(oldL, curgen = 0):
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    print oldL,                    # print the old list, L
    print "  (gen: " + str(curgen) + ")"  # and its gen.
    time.sleep(0.25)
    
    if curgen == 5:  # we're done!
        return       # no return value... yet
    else:
        newL = [ mutate(i, oldL) for i in range(len(oldL)) ]
        return evolve(newL, curgen + 1)
