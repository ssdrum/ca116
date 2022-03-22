#!/usr/bin/env python3

neg_tot = 0
pos_tot = 0

n = int(input())
while n != 0:
   if n < 0:
      neg_tot = neg_tot + n
   else:
      pos_tot = pos_tot + n
   n = int(input())

print(neg_tot, pos_tot)
