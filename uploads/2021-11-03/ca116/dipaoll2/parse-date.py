#!/usr/bin/env python3

s = input()
date = []

# Essentialy a spl1t() function
i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] != " ":
        j = j + 1
    date.append(s[i:j])
    i = j + 1

month = date[2][: len(date[2]) - 1]  # Removing comma at the end
num = date[1]
year = date[3]
day = date[0]

print(month + " " + num + ", " + year + " (" + day + ")")
