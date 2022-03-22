#!/usr/bin/env python3

import sys
n = int(sys.argv[1])

i = 0
while i < n // 2:
    print(" " * (n // 2 - i) + "*" * ((i * 2) + 1))
    i = i + 1

print("*" * n)

i = 0
while i < n // 2:
    print(" " * (i + 1) + "*" * (n - (2 * (i + 1))))
    i = i + 1
