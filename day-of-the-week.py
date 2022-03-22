#!/usr/bin/env python3

month = int(input()) - 1
day = int(input()) - 1
day_of_year = (month * 30) + day

print(day_of_year % 7 + 1)
