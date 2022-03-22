#!/usr/bin/env python3

import sys
paths = sys.argv[1:]  # Handle multiple command line args

i = 0
while i < len(paths):
    tokens = paths[i].split("/")
    path = []

    j = 0
    while j < len(tokens):
        if tokens[j] == ".." and 1 < len(path):
            path.pop()
        elif tokens[j] == ".":
            pass
        else:
            path.append(tokens[j])
        j = j + 1

    if len(path) == 1:
        print("/")
    else:
        print("/".join(path))
    i = i + 1
