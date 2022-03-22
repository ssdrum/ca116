#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    year = s[6:8]
    month = s[3:5]
    day = s[0:2]
    a.append(year + month + day + s[9:])
    s = input()

i = 0
while i < len(a):
    p = i
    j = p + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1

    tmp = a[i]
    a[i] = a[p]
    a[p] = tmp
    i = i + 1

i = 0
while i < len(a):
    print(a[i][6:])
    i = i + 1
