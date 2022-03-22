#!/usr/bin/env python3

import sys

n = int(sys.argv[1])

if n == 2:
    print(2)
else:
    tot = 0
    prev = 1
    curr = 1
    nextNum = 2
    while nextNum < n:
        if nextNum % 2 == 0:
            tot = tot + nextNum
        prev = curr
        curr = nextNum
        nextNum = prev + curr

    print(tot)
