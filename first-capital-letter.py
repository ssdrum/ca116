#!/usr/bin/env python3

s = input()

i = 0
while s[i] < "A" or s[i] > "Z":
    i = i + 1

print(i)
