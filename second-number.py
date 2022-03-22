#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not (s[i] >= "0" and s[i] <= "9"):
    i = i + 1

j = i
while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
    j = j + 1

k = j
while k < len(s) and not (s[k] >= "0" and s[k] <= "9"):
    k = k + 1

i = k
while i < len(s) and (s[i] >= "0" and s[i] <= "9"):
    i = i + 1

if k < len(s):
    print(s[k:i], k)
