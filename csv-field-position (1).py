#!/usr/bin/env python3

import sys

field = sys.argv[1]
data = []
s = input()

prev = 0
i = 0
while i < len(s):
    if i == len(s) - 1:
        data.append(s[prev + 1:i + 1])
    if s[i] == ",":
        if prev == 0:
            data.append(s[prev:i])
        else:
            data.append(s[prev + 1:i])
        prev = i
    i = i + 1

i = 0
while i < len(data) and data[i] != field:
    i = i + 1

if i < len(data):
    print(i)
