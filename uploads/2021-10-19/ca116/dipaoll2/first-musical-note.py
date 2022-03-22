#!/usr/bin/env python3

s = input()
found = False

i = 0
while found != True:
   if s[i] >= "a" and s[i] <= "g":
      found = True
      print(s[i])
   i = i + 1
