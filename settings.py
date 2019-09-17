import sys

try:
    import secret_settings
except:
    sys.exit("secret_settings.py not found.")

PEOPLE_LIST = "resources/people.txt"
DEAD_LIST = "resources/dead.txt"
SENTENCES_LIST = "resources/sentences.txt"
IMAGE = "resources/people.png"
LYNCHING = 69
