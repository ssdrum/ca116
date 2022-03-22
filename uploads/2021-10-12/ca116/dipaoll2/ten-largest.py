#!/usr/bin/env python3

n = 10
largest = 0

i = 0
while i < n:
   m = int(input())
   if m > largest:
      largest = m
   i = i + 1

print(largest)
