import tools.numberGenerator as ng

def selectPerson(people, dead):
    selected = people[ng.getListNumber(people)]

    while selected in dead:
        selected = people[ng.getListNumber(people)]
    return selected

def selectSentence(sentences):
    return sentences[ng.getListNumber(sentences)]
