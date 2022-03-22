#!/usr/bin/env python3

a = []

n = input()
while n != "end":
    a.append(int(n))
    n = input()

p = int(input())
i = p
while i < len(a):
    if a[i] < a[p]:
        p = i
    i = i + 1

print(p)
