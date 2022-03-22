#!/usr/bin/env python3

import sys

translations = {}

# Create dictionary
with open("translation.txt") as f:
    line = f.readline().rstrip()
    while 0 < len(line):
        line = line.split()
        key = line[0]
        val = line[1]
        translations[key] = val
        line = f.readline().rstrip()

# Take inputs and print translations
word = sys.stdin.readline().rstrip()
while 0 < len(word):
    if word in translations:
        print(translations[word])
    word = sys.stdin.readline().rstrip()
