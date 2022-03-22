#!/usr/bin/env python3

words = {}

with open("a.txt") as f:
    word = f.readline().rstrip()
    while 0 < len(word):
        if word not in words:
            words[word] = True
        word = f.readline().rstrip()

with open("b.txt") as f:
    word = f.readline().rstrip()
    while 0 < len(word) and word not in words:
        words[word] = True
        word = f.readline().rstrip()

if 0 < len(word):
    print("intersecting")
else:
    print("disjoint")
