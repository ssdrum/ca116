#!/usr/bin/env python3

home = int(input())
away = int(input())

if home > away:
    print("Home win.")
elif away > home:
    print("Away win.")
else:
    print("Draw.")
