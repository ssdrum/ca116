#!/usr/bin/env python3

s = input()
output = ""

i = 0
while i < len(s):
    if s[i] != " ":
        output = output + s[i]
    i = i + 1

print(output)
