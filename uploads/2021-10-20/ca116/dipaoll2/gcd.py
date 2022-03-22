#!/usr/bin/env python3

a = int(input())
b = int(input())

while b != 0:
    old_a = a
    a = b
    b = old_a % b

print(a)
