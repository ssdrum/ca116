#!/usr/bin/env python3

n = int(input())
n = (n // 100) % 100

print(((n % 10) * 10) + n // 10)
