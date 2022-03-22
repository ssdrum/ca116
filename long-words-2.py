#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["cat", "elephant", "mouse", "lizard", "horse", "mongoose"]

i = 0
while i < len(a) and len(a[i]) < 6:
    i = i + 1

if i < len(a):
    print(a[i])
