#!/usr/bin/env python3

n = int(input())
p = int(input())

r = n % (10 ** (p + 1))

print(r // 10 ** (p))
