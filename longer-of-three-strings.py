#!/usr/bin/env python3

s1 = input()
s2 = input()
s3 = input()

longer = s1

if len(s1) < len(s2):
    longer = s2
    if len(s2) < len(s3):
        longer = s3
elif len(s2) < len(s3):
    longer = s3
    if len(s3) < len(s1):
        longer = s1

print(longer)
