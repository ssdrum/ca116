#!/usr/bin/env python3


a = []

s = input()
while s != "end":
    b = []
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and s[j] != ",":
            j = j + 1
        if s[i] == ",":
            b.append(s[i + 1:j])
        else:
            b.append(s[i:j])
        i = j
    a.append(b)
    i = i + 1
    s = input()

field = int(input())

i = 0
while i < len(a):
    print(a[i][field])
    i = i + 1
