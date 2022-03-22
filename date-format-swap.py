#!/usr/bin/env python3

n = int(input())

month = n // 10000
day = (n // 100) % 100
year = n % 100

print(day * 10000 + month * 100 + year)
