#!/usr/bin/env python3

prev = int(input())

if prev != 0:
   curr = int(input())

   while curr != 0:
      if curr > prev:
         print("higher")
      elif curr == prev:
         print("equal")
      else:
         print("lower")
      prev = curr
      curr = int(input())
