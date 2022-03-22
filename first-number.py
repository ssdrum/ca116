#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not (s[i] >= "0" and s[i] <= "9"):
    i = i + 1

j = i
while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
    j = j + 1

if j < len(s):
    print(s[i:j], i)
