#!/usr/bin/env python3

a = []
b = []

counter = 0
while counter < 2:
    n = input()
    while  n != "end":
        if counter == 0:
            a.append(int(n))
        else:
            b.append(int(n))
        n = input()
    counter = counter + 1

i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        print(a[i])
        i = i + 1
    else:
        print(b[j])
        j = j + 1
