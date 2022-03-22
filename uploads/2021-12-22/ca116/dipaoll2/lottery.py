#!/usr/bin/env python3

import sys

drawn = {
    sys.argv[1]: True,
    sys.argv[2]: True,
    sys.argv[3]: True,
}

ticket = sys.stdin.readline().rstrip()
while 0 < len(ticket):
    tokens = ticket.split()
    matches = 0

    if tokens[0] in drawn:
        matches = matches + 1
    if tokens[1] in drawn:
        matches = matches + 1
    if tokens[2] in drawn:
        matches = matches + 1

    if matches == 0:
        print(0)
    elif matches == 1:
        print(1)
    elif matches == 2:
        print(5)
    else:
        print(100)
    ticket = sys.stdin.readline().rstrip()
