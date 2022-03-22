#!/usr/bin/env python3

s = input()
length = len(s)
output = s[length - 1] + s[1:length - 1] + s[0]

print(output)
