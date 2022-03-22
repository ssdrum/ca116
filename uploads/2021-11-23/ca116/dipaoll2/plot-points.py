#!/usr/bin/env python3

import sys

points = {}

point = sys.stdin.readline().rstrip()
while 0 < len(point):
    points[point] = True
    point = sys.stdin.readline().rstrip()

print(" " + "-" * 20)

y = 19
while y >= 0:
    x = 0
    while x < 21:
        if x == 0 or x == 20:
            print("|", end="")
        if str(x) + " " + str(y) in points:
            print("*", end="")
        if str(x) + " " + str(y) not in points and x < 20:
            print(" ", end="")
        x = x + 1
    print()
    y = y - 1

print(" " + "-" * 20)
