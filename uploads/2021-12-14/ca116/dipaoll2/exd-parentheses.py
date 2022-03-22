#!/usr/bin/env python3

import sys

s = sys.stdin.readline().rstrip()
while 0 < len(s):
    i = 0
    while i < len(s) and s[i] != "(":
        i = i + 1
    if i < len(s):
        j = i
        while j < len(s) and s[j] != ")":
            j = j + 1
        print(s[i + 1:j])
    s = sys.stdin.readline().rstrip()
