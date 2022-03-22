#!/usr/bin/env python3

n = 10
total = 0

i = 0
while i < n:
    m = int(input())

    if m % 2 == 0:
        total = total + m
    i = i + 1

print(total)
