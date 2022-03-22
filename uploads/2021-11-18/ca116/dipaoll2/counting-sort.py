#!/usr/bin/env python3

#  the first loop:
#    creates a list of lists, each containing:
#    1. a number starting at 0 that increases by one at each cycle
#    2. a counter
#  increases count of a number by one if it matches the input

#  the second loop:
#    1. loops through each number and prints it if count > 0
#    1. decreases count by one and prints the number again

numbers = []

i = 0
n = input()
while n != "end":
    count = 0
    numbers.append([i, count])

    if int(n) <= i:
        numbers[int(n)][1] = numbers[int(n)][1] + 1
        n = input()
    i = i + 1

i = 0
while i < len(numbers):
    if 0 < numbers[i][1]:
        print(str(numbers[i][0]))
        numbers[i][1] = numbers[i][1] - 1
        i = i - 1
    i = i + 1
