#!/usr/bin/env python3

tot = 0

s = input()
while s != "end":
    tot = tot + int(s.split()[2])
    s = input()

print(tot)
