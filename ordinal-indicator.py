#!/usr/bin/env python3

n = int(input())

if n % 100 >= 11 and n % 100 <= 13:
    print("th")
elif n % 10 == 1:
    print("st")
elif n % 10 == 2:
    print("nd")
elif n % 10 == 3:
    print("rd")
else:
    print("th")
