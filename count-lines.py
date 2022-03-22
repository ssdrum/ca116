#!/usr/bin/env python3

import sys

top = []
mid = {}
bott = {}
largest = 0

i = 0
while i < 3:
    coords = sys.stdin.readline().split()
    if i == 0:
        j = 0
        while j < len(coords):
            top.append(int(coords[j]))
            j = j + 1
    elif i == 1:
        largest = int(coords[len(coords) - 1])
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

i = 0
while i < len(top):
    j = 0
    while j < len(mid):
        if top[i] + j in mid and top[i] + j * 2 in bott:
            lines = lines + 1
            # print(top[i], top[i] + j, top[i] + j * 2)
        if top[i] - j in mid and top[i] - j * 2 in bott and j != 0:
            # print(top[i], top[i] - j, top[i] - j * 2)
            lines = lines + 1
        j = j + 1
    i = i + 1

print(lines)
