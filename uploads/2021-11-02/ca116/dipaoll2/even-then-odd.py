#!/usr/bin/env python3

o = []

s = input()
while s != "end":
    if int(s) % 2 == 0:
        print(s)
    else:
        o.append(s)
    s = input()

i = 0
while i < len(o):
    print(o[i])
    i = i + 1
