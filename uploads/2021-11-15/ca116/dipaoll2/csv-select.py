#!/usr/bin/env python3

import sys

arg = sys.argv[1]
data = []

i = 0  # Extract header and value from command line argument
while i < len(arg) and arg[i] != "=":
    i = i + 1
header = arg[:i]
value = arg[i + 1:]

s = input()  # Divide lines into a list
while s != "end":
    line = []
    prev = 0
    i = 0
    while i < len(s):
        if i == len(s) - 1:
            line.append(s[prev + 1:i + 1])
        if s[i] == ",":
            if prev == 0:
                line.append(s[prev:i])
            else:
                line.append(s[prev + 1:i])
            prev = i
        i = i + 1
    data.append(line)
    s = input()

i = 0  # Find position of header
while i < len(data[0]) and data[0][i] != header:
    i = i + 1
pos = i

i = 1  # Print
while i < len(data):
    if data[i][pos] == value:
        line = ""
        j = 0
        while j < len(data[i]):
            if j == len(data[i]) - 1:
                line = line + data[i][j]
            else:
                line = line + data[i][j] + ","
            j = j + 1
        print(line)
    i = i + 1
