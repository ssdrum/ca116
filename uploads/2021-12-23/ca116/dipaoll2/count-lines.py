#!/usr/bin/env python3

import sys

top = {}
mid = {}
bott = {}
lim = 0

i = 0
while i < 3:
    coords = sys.stdin.readline().split()
    if i == 0:
        lim = int(coords[len(coords) - 1]) // 2 + 1
        j = 0
        while j < len(coords):
            top[int(coords[j])] = True
            j = j + 1
    elif i == 1:
        j = 0
        while j < len(coords):
            mid[int(coords[j])] = True
            j = j + 1
    else:
        j = 0
        while j < len(coords):
            bott[int(coords[j])] = True
            j = j + 1
    i = i + 1

lines = 0

for n in top:
    i = 0
    while i < lim:
        if n + i in mid and n + i * 2 in bott:
            lines = lines + 1
        if n - i in mid and n - i * 2 in bott and i != 0:
            lines = lines + 1
        i = i + 1

print(lines)
