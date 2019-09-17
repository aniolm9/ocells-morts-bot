#!/usr/bin/env python3
import random
import tools.fileProcessor as fp

# Number used to decide if it's a normal kill or a lynching.
def getProbabilityNumber():
    return random.randint(1, 155*5)

# Number used to select the victim and the killer and the sentence.
def getListNumber(l):
    n = len(fp.readFile(l))
    return random.randint(0, n-1)
