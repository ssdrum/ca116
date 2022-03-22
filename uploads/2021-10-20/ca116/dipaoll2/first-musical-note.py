#!/usr/bin/env python3

s = input()

i = 0
while s[i] < "a" or s[i] > "g":
    i = i + 1

print(s[i])
