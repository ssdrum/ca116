#!/usr/bin/env python3

lines = []

s = input()
while s != "end":
    lines.append(s)
    s = input()

i = 0
while i < len(lines):
    print(lines[len(lines) - i - 1])
    i = i + 1
