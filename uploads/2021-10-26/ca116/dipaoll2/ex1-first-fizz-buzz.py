#!/usr/bin/env python3

n = int(input())

while n % 3 != 0 or n % 5 != 0:
    n = int(input())

print(n)
