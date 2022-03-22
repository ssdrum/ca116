#!/usr/bin/env python3

a = []

n = input()
while n != "end":
    a.append(int(n))
    n = input()

i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j  # store the index in p
        j = j + 1
    tmp = a[i]  # swap a[i] with a[p] (i.e. swap a[i] with the smallest number)
    a[i] = a[p]
    a[p] = tmp
    i = i + 1

print(a[len(a) // 2])
