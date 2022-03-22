#!/usr/bin/env python3

import sys

pages = []

i = 0
while i < 10:  # Creates list of list of strings (pages -> page -> line)
    with open("page-" + str(i) + ".txt") as f:
        page = f.readlines()
        pages.append(page)
    i = i + 1

triplet = sys.stdin.readline().rstrip()
while 0 < len(triplet):
    tokens = triplet.split()
    page = int(tokens[0])
    line = int(tokens[1])
    char = int(tokens[2])
    print(pages[page][line][char], end="")
    triplet = sys.stdin.readline().rstrip()
