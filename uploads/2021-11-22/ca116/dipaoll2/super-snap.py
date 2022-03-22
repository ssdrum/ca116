#!/usr/bin/env python3

import sys

seen = {}

word = sys.stdin.readline().rstrip()
while 0 < len(word) and word not in seen:
    seen[word] = True
    word = sys.stdin.readline().rstrip()

if 0 < len(word):  # print only if last word is not empty string
    print("snap: " + word)
