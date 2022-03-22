#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(s)
    s = input()

day = input()

i = 0
while i < len(a):
    if a[i].split()[0] == day:
        print(a[i])
    i = i + 1
