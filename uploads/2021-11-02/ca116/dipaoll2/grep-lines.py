#!/usr/bin/env python3

import sys
p = sys.argv[1]
lines = []

s = input()
while s != "end":
    lines.append(s)
    s = input()

i = 0
while i < len(lines):
    line = lines[i]

    j = 0
    while j < len(line) - len(p) + 1:
        if line[j:j + len(p)] == p:
            print(lines[i])
        j = j + 1
    i = i + 1
