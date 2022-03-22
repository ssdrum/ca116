#!/usr/bin/env python3

import sys

english = "one two three four five six seven eight nine ten".split()
german = "eins zwei drei vier funf sechs sieben acht neun zehn".split()

translations = {}

i = 0
while i < len(english):
    translations[english[i]] = german[i]
    i = i + 1

word = sys.stdin.readline().rstrip()
while 0 < len(word):
    if word in english:
        print(translations[word])
    word = sys.stdin.readline().rstrip()
