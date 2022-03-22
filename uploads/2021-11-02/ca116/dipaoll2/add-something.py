#!/usr/bin/env python3

numbers = []

s = input()
while s != "end":
    numbers.append(int(s))
    s = input()

n = int(input())

i = 0
while i < len(numbers):
    print(numbers[i] + n)
    i = i + 1
