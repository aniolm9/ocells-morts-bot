#!/usr/bin/env python3
import tools.numberGenerator as ng
import tools.listSelector as ls
import tools.fileProcessor as fp
import constants
import sys

def win():
    return len(fp.readFile(constants.PEOPLE_LIST)) - len(fp.readFile(constants.DEAD_LIST)) == 1

def kill():
    killer = ls.selectFromList(constants.PEOPLE_LIST)
    victim = ls.selectFromList(constants.PEOPLE_LIST)
    beerSentence = victim + " deu una cervesa a " + killer + "."

    if win():
        print (killer + " ha guanyat la partida.")
        return constants.FI

    if killer == victim:
        print (victim + " considera que el joc és una puta merda i s'ha suïcidat.")
    elif ng.getProbabilityNumber() == constants.LYNCHING:
        print (victim + " ha estat linxat públicament per fer un tuit massa dolent." + victim + " deu una cervesa a tothom.")
    # Opció troll 1:
    elif victim == "@Virgili7":
        print (killer + " a pegat un tiro a @Virgili7 i a morit. " + beerSentence)
    # Opció troll 2:
    elif victim == "@Joan_BonaNit":
        print (killer + " ha introduit un megàfon a l'esòfag de @Joan_BonaNit. " + beerSentence)
    else:
        sentence = ls.selectFromList(constants.SENTENCES_LIST)
        print (killer + " " + sentence + " " + victim + ". " + beerSentence)

    # Escriu la víctima a la llista de morts.
    fp.appendToFile(constants.DEAD_LIST, victim + "\n")

kill()
