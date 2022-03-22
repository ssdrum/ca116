#!/usr/bin/env python3

a = int(input())
b = int(input())

if a % 2 == 0:
    if b == a // 2:
        print("yes")
    else:
        print("no")
else:
    if b == 3 * a + 1:
        print("yes")
    else:
        print("no")
