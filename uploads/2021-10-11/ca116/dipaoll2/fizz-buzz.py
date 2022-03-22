#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
    j = i + 1
    if j % 3 == 0 and j % 5 == 0:
        print("fizz-buzz")
    elif j % 3 == 0 and j % 5 != 0:
        print("fizz")
    elif j % 3 != 0 and j % 5 == 0:
        print("buzz")
    else:
        print(j)
    i = i + 1
