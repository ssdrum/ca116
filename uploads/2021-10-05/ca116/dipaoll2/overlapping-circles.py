#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

distance = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
radii_sum = (r1 + r2) * (r1 + r2)

if distance < radii_sum:
    print("yes")
else:
    print("no")
