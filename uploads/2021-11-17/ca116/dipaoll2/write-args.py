#!/usr/bin/env python3

import sys

out_file = sys.argv[1]
args = sys.argv[2:]

with open(out_file, "w") as f:
    i = 0
    while i < len(args):
        f.write(args[i] + "\n")
        i = i + 1
