#!/usr/bin/env python3

# Creates a list containing 999 lists, each containing:
# 1) A number starting from 0, to 999
# 2) A counter that starts at 0

numbers = []

i = 0
n = input()
while i <= 999 and n != "end":
    count = 0
    numbers.append([i, count])

    if int(n) <= i:
        numbers[int(n)][1] = numbers[int(n)][1] + 1
        n = input()
    i = i + 1

i = 0
while i < len(numbers):
    if 0 < numbers[i][1]:
        print(numbers[i][0])
    i = i + 1
