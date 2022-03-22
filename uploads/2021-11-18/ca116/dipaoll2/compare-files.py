#!/usr/bin/env python3

import sys

# Open files
with open(sys.argv[1]) as f:
    a = f.read()

with open(sys.argv[2]) as f:
    b = f.read()

#  Count number of lines
num_lines = 0
i = 0
while i < len(a) and i < len(b) and a[i] == b[i]:
    if a[i] == "\n":
        num_lines = num_lines + 1
    i = i + 1

# Print position of first different char
if i < len(a) or i < len(b):
    lines = a.split("\n")

    # subtract the length of each previous line to i
    j = 0
    while j < num_lines:
        i = i - (len(lines[j]) + 1)
        j = j + 1

    print(num_lines, i)
