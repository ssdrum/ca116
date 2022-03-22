#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
    print(i * -(i % 2) + (((i + 1) % 2) * i))
    i = i + 1
