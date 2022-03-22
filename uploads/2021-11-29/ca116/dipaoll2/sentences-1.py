#!/usr/bin/env python3

import sys

stop_chars = {
    ".": True,
    "!": True,
    "?": True
}

text = " ".join(" ".join(sys.stdin.readlines()).split()) + " "

s = ""
i = 0
while i < len(text):
    s = s + text[i]

    if text[i] in stop_chars and text[i + 1] == " ":
        print(s.lstrip())
        s = ""
    i = i + 1
