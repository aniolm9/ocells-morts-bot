#!/usr/bin/env python3
import random

# Number used to decide if it's a normal kill or a lynching.
def getProbabilityNumber():
    return random.randint(1, 155)

# Number used to select the victim and the killer and the sentence.
def getListNumber(l):
    n = len(l)
    return random.randint(0, n-1)
