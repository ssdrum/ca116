#!/usr/bin/env python3

import sys

out_file = sys.argv[1]

with open(out_file, "w") as f_out:
    f_out.write("Hello world.\n")
