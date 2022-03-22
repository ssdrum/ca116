#!/usr/bin/env python3

import sys

field = sys.argv[1]
a = []
s = input()

prev = 0
i = 0
while i < len(s):
    if i == len(s) - 1:
        a.append(s[prev + 1:i + 1])
    if s[i] == ",":
        if prev == 0:
            a.append(s[prev:i])
        else:
            a.append(s[prev + 1:i])
        prev = i
    i = i + 1

i = 0
while i < len(a) and a[i] != field:
    i = i + 1

print(i)
