#!/usr/bin/env python3

f = input()

i = 0
while i < len(f) and f[i] != ".":
    i = i + 1

print(f[:i])
print(f[i + 1:])
