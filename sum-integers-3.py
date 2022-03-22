#!/usr/bin/env python3

import sys

args = sys.argv[1:]
tot = 0

i = 0
while i < len(args):
    with open(args[i]) as f:
        n = f.readline().rstrip()
        while 0 < len(n):
            tot = tot + int(n)
            n = f.readline().rstrip()
    i = i + 1

print(tot)
