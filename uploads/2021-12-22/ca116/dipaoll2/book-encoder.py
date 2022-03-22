#!/usr/bin/env python3

import sys

pages = []

i = 0
while i < 10:  # creates list of list of strings (page -> line -> char)
    with open(f"page-{i}.txt") as f:
        page = f.readlines()
        pages.append(page)
    i = i + 1

plaintext = ""
s = sys.stdin.readline()
while 1 < len(s):  # must keep newline characters
    plaintext = plaintext + s
    s = sys.stdin.readline()

used = {}

i = 0  # i = current char in the plaintext
while i < len(plaintext):
    found = False
    p = 0  # p = current page
    while p < 10 and not found:
        j = 0  # l = current line
        while j < len(pages[p]) and not found:
            c = 0  # c = current character
            while c < len(pages[p][j]) and plaintext[i] != pages[p][j][c]:
                c = c + 1
            if c < len(pages[p][j]) and f"{p} {j} {c}" not in used:
                used[f"{p} {j} {c}"] = True
                print(f"{p} {j} {c}")
                found = True
            j = j + 1
        p = p + 1
    i = i + 1
