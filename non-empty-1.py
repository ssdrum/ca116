#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

counter = 0

i = 0
while i < len(a):
    if a[i] != "":
        counter = counter + 1
    i = i + 1

print(counter)
