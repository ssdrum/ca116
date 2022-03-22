#!/usr/bin/env python3

import sys

names = {}

with open("boys.txt") as f:
    name = f.readline().rstrip()
    while 0 < len(name):
        names[name] = "boy"
        name = f.readline().rstrip()

with open("girls.txt") as f:
    name = f.readline().rstrip()
    while 0 < len(name):
        if name in names:
            names[name] = "either"
        else:
            names[name] = "girl"
        name = f.readline().rstrip()

s = sys.stdin.readline().rstrip()
while 0 < len(s):
    print(s, names[s])
    s = sys.stdin.readline().rstrip()
