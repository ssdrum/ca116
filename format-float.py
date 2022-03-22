#!/usr/bin/env python3

n = input()

i = 0
while i < len(n) and n[i] != ".":
    i = i + 1
if i == 0:
    print("0" + n)
elif i == len(n):
    print(n + ".0")
elif i == len(n) - 1:
    print(n + "0")
elif n[0] == "-" and n[1] == ".":
    print(n[:1] + "0" + n[1:])
else:
    print(n)
