#!/usr/bin/env python3

with open("input.txt") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    print(lines[i].rstrip("\n"))
    i = i + 1
