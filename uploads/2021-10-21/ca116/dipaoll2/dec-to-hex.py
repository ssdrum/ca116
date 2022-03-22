#!/usr/bin/env python3

dec = int(input())
result = ""
hex = "0123456789abcdef"

while dec != 0:
    rem = dec % 16
    dec = dec // 16
    result = hex[rem] + result

print(result)
