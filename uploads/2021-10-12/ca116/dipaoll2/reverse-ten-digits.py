#!/usr/bin/env python3

n = 10
sequence = 0

i = 0
while i < n:
    sequence = sequence * 10
    sequence = sequence + int(input())
    i = i + 1

j = 0
while j < n:
    print(sequence % 10)
    sequence = sequence // 10
    j = j + 1
