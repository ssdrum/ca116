#!/usr/bin/env python3

s = input()
while s != "end":
    a = s.split()
    if a[1][0] == "0":
        a[1] = a[1][1:]
    start = a[1] + ":00"
    end = str(int(a[1]) + int(a[2]) - 1) + ":50"
    a[1] = start
    a[2] = end
    print(" ".join(a))
    s = input()
