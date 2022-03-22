#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
    if i == n // 2:
        print("*" * n)
    else:
        print(" " * (n // 2) + "*")
    i = i + 1
