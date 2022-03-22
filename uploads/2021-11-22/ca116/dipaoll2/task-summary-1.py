#!/usr/bin/env python3

import sys

results = {}

line = sys.stdin.readline().rstrip()
while 0 < len(line):
    line = line.split(".")
    task = line[0] + "." + line[1]
    state = line[2]
    results[task] = state
    line = sys.stdin.readline().rstrip()

for task in results:
    if results[task] == "correct":
        print(task)
