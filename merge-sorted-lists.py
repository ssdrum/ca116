#!/usr/bin/env python3

a = []
b = []

i = 0
while i < 2:
    n = input()
    while n != "end":
        if i == 0:
            a.append(int(n))
        else:
            b.append(int(n))
        n = input()
    i = i + 1

i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        print(a[i])
        i = i + 1
    else:
        print(b[j])
        j = j + 1

if len(a) != len(b):
    if len(a) < len(b):
        while j < len(b):
            print(b[j])
            j = j + 1
    else:
        while i < len(a):
            print(a[i])
            i = i + 1
