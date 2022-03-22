#!/usr/bin/env python3

import sys

text = sys.stdin.read()
print("\n".join(" ".join(text.split("\n")).split()))
