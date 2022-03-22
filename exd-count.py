#!/usr/bin/env python3

import sys

n = int(sys.argv[1])

i = 0
while i * i < n:
    print(i)
    i = i + 1
