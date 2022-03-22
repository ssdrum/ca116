#!/usr/bin/env python3

upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
lower = "abcdefghifklmnopqrstuvwxyz"

s = input()
while s != "end":
    i = 0
    while i < len(s):
        j = 0
        while j < 26:
            if s[i] == upper[j]:
                s = s[:i] + lower[j] + s[i + 1:]
            j = j + 1
        i = i + 1
    print(s)
    s = input()
