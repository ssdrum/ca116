#!/usr/bin/env python3

neg_tot = 0
pos_tot = 0

i = 0
while i < 5:
   n = int(input())
   if n < 0:
      neg_tot = neg_tot + n
   else:
      pos_tot = pos_tot + n
   i = i + 1

print(neg_tot, pos_tot)
