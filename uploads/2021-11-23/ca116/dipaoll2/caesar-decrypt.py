#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower[n:] + lower[:n] + upper[n:] + upper[:n]
dst = lower + upper

translation = {}

i = 0
while i < len(src):
    translation[src[i]] = dst[i]
    i = i + 1

cipher = sys.stdin.read().rstrip()
plaintext = ""

i = 0
while i < len(cipher):
    if cipher[i] in translation:
        plaintext = plaintext + translation[cipher[i]]
    else:
        plaintext = plaintext + cipher[i]
    i = i + 1

print(plaintext)
