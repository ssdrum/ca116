#!/usr/bin/env python3

s = input()
rev = ""

i = 0
while i < len(s):
    rev = rev + s[len(s) - i - 1]
    i = i + 1

print(rev)
