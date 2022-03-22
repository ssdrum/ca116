#!/usr/bin/env python3

dec = int(input())
bin = ""

while dec != 0:
    rem = dec % 2
    dec = dec // 2
    bin = str(rem) + bin

print(bin)
