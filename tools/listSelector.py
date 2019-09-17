#!/usr/bin/env python3
import tools.numberGenerator as ng
import tools.fileProcessor as fp
import constants

def selectFromList(file):
    l = fp.readFile(file)
    selected = l[ng.getListNumber(file)]

    if file != constants.PEOPLE_LIST:
        return selected

    deadList = fp.readFile(constants.DEAD_LIST)
    while selected in deadList:
        selected = l[ng.getListNumber(file)]
    return selected
