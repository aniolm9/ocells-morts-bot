import tools.numberGenerator as ng
import tools.listSelector as ls
import tools.fileProcessor as fp
import tools.textToImage as tti
import settings
import sys

def win(people):
    dead = fp.readFile(settings.DEAD_LIST)
    if len(people) - len(dead) == 1:
        winner = ls.selectPerson(people, dead)
        return "\n\n" + winner + " és l'últim supervivent. " + winner + " ha guanyat la partida."
    return ""

def kill():
    people = fp.readFile(settings.PEOPLE_LIST)
    dead = fp.readFile(settings.DEAD_LIST)

    if len(people) - len(dead) > 1:
        killer = ls.selectPerson(people, dead)
        victim = ls.selectPerson(people, dead)
        beerSentence = victim + " deu una cervesa a " + killer + "."
        string = "."

        if killer == victim:
            string += victim + " ha estat víctima d'un apunyalament a Barcelona."
        elif (ng.getProbabilityNumber() == settings.LYNCHING) and (len(dead) < len(people) - 5):
            string += victim + " ha estat linxat públicament per fer un tuit massa dolent. " + victim + " deu una cervesa a tothom."
        # Opció troll 1:
        elif victim == "@Virgili7":
            string += killer + " a pegat un tiro a @Virgili7 i a morit. " + beerSentence
        # Opció troll 2:
        elif victim == "@Joan_BonaNit":
            string += killer + " ha introduit un megàfon a l'esòfag de @Joan_BonaNit. " + beerSentence
        else:
            sentence = ls.selectSentence(fp.readFile(settings.SENTENCES_LIST))
            string += killer + " " + sentence + " " + victim + ". " + beerSentence

        # Escriu la víctima a la llista de morts.
        fp.appendToFile(settings.DEAD_LIST, victim + "\n")
        tti.drawImage(settings.IMAGE)

        # Check if somebody wins.
        string += win(people)
        return string
    else:
        sys.exit("El joc s'ha acabat.")
