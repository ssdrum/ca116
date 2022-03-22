#!/usr/bin/env python3

data = [0] * 10

s = input()
while s != "end":
    s = int(s)
    data[s] = data[s] + 1
    s = input()

i = 0
while i < 10:
    print(i, "*" * data[i])
    i = i + 1
