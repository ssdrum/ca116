#!/usr/bin/env python3

total = 0

i = 0
while i < 5:
   n = int(input())
   if n < 0:
      n = -n
   total = total + n
   i = i + 1

print(total)
