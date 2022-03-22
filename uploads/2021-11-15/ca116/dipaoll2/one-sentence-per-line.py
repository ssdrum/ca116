#!/usr/bin/env python3

# Lord forgive me for this code.

text = ""

s = input()
while s != "end":
    text = text + " " + s
    s = input()

text = " ".join(text.split()).split(".")

i = 0
while i < len(text):
    if len(text[i]) > 0:
        if text[i][0] == " ":
            # The next line eliminates some random extra white spaces
            # at the start of every line
            text[i] = text[i][1:]
        print(text[i] + ".")
    i = i + 1
