#!/usr/bin/env python3

n = input()
exp = len(n) - 1
dec = 0

i = 0
while i < len(n):
    dec = dec + int(n[i]) * (2 ** exp)
    exp = exp - 1
    i = i + 1

print(dec)
