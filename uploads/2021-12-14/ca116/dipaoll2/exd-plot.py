#!/usr/bin/env python3

import sys

length = int(input())
points = {}

n = sys.stdin.readline().rstrip()
while 0 < len(n):
    points[int(n)] = True
    n = sys.stdin.readline().rstrip()

print("|", end="")

i = 0
while i < length:
    if i in points:
        print("*", end="")
    else:
        print(" ", end="")
    i = i + 1

print("|")
