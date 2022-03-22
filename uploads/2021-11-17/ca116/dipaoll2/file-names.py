#!/usr/bin/env python3

import sys

s = sys.stdin.readline().rstrip()
while 0 < len(s):
    a = s.split("/")
    print(a[len(a) - 1])
    s = sys.stdin.readline().rstrip()
