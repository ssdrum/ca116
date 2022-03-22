#!/usr/bin/env python3

import sys

words = {}

word = sys.stdin.readline().rstrip()
while 0 < len(word):
    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = 1
    word = sys.stdin.readline().rstrip()

for word in words:
    if words[word] == 1:
        print(word)
