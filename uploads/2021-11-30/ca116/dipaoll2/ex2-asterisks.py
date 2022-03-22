#!/usr/bin/env python3

with open("output.txt", "w") as f_out:
    with open("input.txt") as f_in:
        c = f_in.read(1)
        while 0 < len(c):
            if ("a" <= c and c <= "z") or ("A" <= c and c <= "Z"):
                f_out.write("*")
            else:
                f_out.write(c)
            c = f_in.read(1)
