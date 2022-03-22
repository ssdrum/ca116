#!/usr/bin/env python3

s = input()
while s != "end":
    print(" ".join(s.split()[5:]))
    s = input()
