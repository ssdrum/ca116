#!/usr/bin/env python3

mark = int(input())

first = mark >= 70
second = mark >= 50 and mark <= 69
third = mark >= 40 and mark <= 49
fail = mark < 40

print("first: " + str(first))
print("second: " + str(second))
print("third: " + str(third))
print("fail: " + str(fail))
