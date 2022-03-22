#!/usr/bin/env python3

lines = []
num_lines = 0
s = input()

while s != "end":
    lines.append(s)
    num_lines = num_lines + 1
    s = input()

i = 0
while i < len(lines):
    print(i, num_lines, lines[i])
    i = i + 1
