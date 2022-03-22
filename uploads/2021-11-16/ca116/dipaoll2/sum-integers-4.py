#!/usr/bin/env python3

import sys

args = sys.argv[1:]
tot = 0

i = 0
while i < len(args):
    with open(args[i]) as f:
        line = f.readline().rstrip()
        while 0 < len(line):
            a = line.split()
            j = 0
            while j < len(a):
                tot = tot + int(a[j])
                j = j + 1
            line = f.readline().rstrip()
    i = i + 1

print(tot)
