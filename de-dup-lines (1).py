#!/usr/bin/env python3

lines = []

s = input()
while s != "end":
    i = 0
    while i < len(lines) and lines[i] != s:
        i = i + 1
    if i == len(lines):
        lines.append(s)
    s = input()

i = 0
while i < len(lines):
    print(lines[i])
    i = i + 1
