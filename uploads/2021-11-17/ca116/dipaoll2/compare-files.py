#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    a = f.read()

with open(sys.argv[2]) as f:
    b = f.read()

num_lines = 0
i = 0
while i < len(a) and a[i] == b[i]:
    if a[i] == "\n":
        num_lines = num_lines + 1
    i = i + 1

if i < len(a):
    lines = a.split("\n")
    if 0 < num_lines:
        i = i - len(lines[num_lines - 1]) - 1
    print(num_lines, i)
