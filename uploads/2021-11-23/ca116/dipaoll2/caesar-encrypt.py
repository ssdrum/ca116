#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

encription = {}

i = 0
while i < len(src):
    encription[src[i]] = dst[i]
    i = i + 1

plaintext = sys.stdin.read().rstrip()
cipher = ""

i = 0
while i < len(plaintext):
    if plaintext[i] in encription:
        cipher = cipher + encription[plaintext[i]]
    else:
        cipher = cipher + plaintext[i]
    i = i + 1

print(cipher)
