#!/usr/bin/env python3

import sys

fruits = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

word = sys.stdin.readline().rstrip()
while 0 < len(word):
    if word in fruits:
        print(word)
    word = sys.stdin.readline().rstrip()
