#!/usr/bin/env python3

s = input()
n = int(input())
output = (s + "-") * n

print(output[:len(output) - 1])
