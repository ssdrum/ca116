#!/usr/bin/env python3

import sys

punct_chars = {
    ".": True,
    ",": True,
    "!": True,
    "?": True,
    ";": True,
    ":": True
}

text = sys.stdin.read().rstrip()

count = 0
i = 0
while i < len(text):
    if text[i] in punct_chars:
        count = count + 1
    i = i + 1

print(count)
