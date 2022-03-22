#!/usr/bin/env python3

s = input()
capitals = 0

i = 0
while i < len(s):
    if s[i] >= "A" and s[i] <= "Z":
        capitals = capitals + 1
    i = i + 1

print(capitals)
