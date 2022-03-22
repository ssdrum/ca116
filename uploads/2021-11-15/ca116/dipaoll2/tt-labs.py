#!/usr/bin/env python3

s = input()
while s != "end":
    if int(s.split()[2]) > 1:
        print(s)
    s = input()
