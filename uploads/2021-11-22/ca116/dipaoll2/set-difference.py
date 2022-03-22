#!/usr/bin/env python3

words = {}

with open("b.txt") as f:
    word = f.readline().rstrip()
    while 0 < len(word):
        if word not in words:
            words[word] = True
        word = f.readline().rstrip()

with open("a.txt") as f:
    word = f.readline().rstrip()
    while 0 < len(word):
        if word not in words:
            print(word)
        word = f.readline().rstrip()
