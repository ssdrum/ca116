#!/usr/bin/env python3

import sys

n = sys.stdin.readline().rstrip()
while 0 < len(n) and int(n) < 100:
    n = sys.stdin.readline().rstrip()

if len(n) == 0:
    print("none")
else:
    print(n)
