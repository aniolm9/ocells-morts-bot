#!/usr/bin/env python3

# Reads a file and returns a list with the lines.
def readFile(file):
    f = open(file, 'r')
    lines = f.readlines()
    content = [x.strip() for x in lines]
    f.close()
    return content

def appendToFile(file, text):
    f = open(file, 'a+')
    f.write(text)
    f.close()
