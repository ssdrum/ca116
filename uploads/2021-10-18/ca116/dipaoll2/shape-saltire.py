#!/usr/bin/env python3

n = int(input())

i = 0
while i < n // 2:
    print(" " * i + "*" + " " * (n - 2 - (2 * i)) + "*")
    i = i + 1

print(" " * (n // 2) + "*")

i = 0
while i < n // 2:
    print(" " * ((n // 2) - (i + 1)) + "*" + " " * (i + 1 * (i + 1)) + "*")
    i = i + 1
