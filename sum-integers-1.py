#!/usr/bin/env python3

import sys

tot = 0

n = sys.stdin.readline().rstrip()
while len(n) != 0:
    tot = tot + int(n)
    n = sys.stdin.readline().rstrip()

print(tot)
