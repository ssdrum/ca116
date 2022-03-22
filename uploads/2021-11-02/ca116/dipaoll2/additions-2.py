#!/usr/bin/env python3

s = input()
tot = 0

i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] != "+":
        j = j + 1
    tot = tot + int(s[i:j])
    i = j + 1

print(tot)
