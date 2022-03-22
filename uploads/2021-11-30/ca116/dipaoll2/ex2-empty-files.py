#!/usr/bin/env python3

import sys

file_names = sys.argv[1:]

i = 0
while i < len(file_names):
    with open(file_names[i]) as f:
        if len(f.read()) == 0:
            print(file_names[i])
    i = i + 1
