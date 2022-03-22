#!/usr/bin/env python3

a = []

n = input()
while n != "end":
    a.append(int(n))
    n = input()

p = 0
i = 1
while i < len(a):
    if a[i] < a[p]:
        p = i
    i = i + 1

print(p)
