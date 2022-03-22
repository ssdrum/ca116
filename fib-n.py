#!/usr/bin/env python3

n = int(input())
m = 0
o = 1

i = 0
while i < n:
    print(m)
    m = m + o
    o = m - o
    i = i + 1
