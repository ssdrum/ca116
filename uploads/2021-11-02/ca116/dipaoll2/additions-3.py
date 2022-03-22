#!/usr/bin/env python3

sum = 0
while sum != 1000:
    s = input()

    i = 0
    while i < len(s) and s[i] != "+":
        i = i + 1
    sum = int(s[:i]) + int(s[i + 1:])

    print(sum)
    i = i + 1
