#!/usr/bin/env python3

in_file = "irish-dobs.txt"
out_file = "american-dobs.txt"


with open(out_file, "w") as f_out:
    with open(in_file) as f_in:
        line = f_in.readline()
        while 0 < len(line):
            # Extract date
            a = line.split()
            date = a[0].split("/")
            # swap day and month
            day = line.split()[0].split("/")[0]
            mon = line.split()[0].split("/")[1]
            date[0] = mon
            date[1] = day
            form_date = "/".join(date)
            a[0] = form_date
            form_line = " ".join(a)
            # write formatted data to output file
            f_out.write(form_line + "\n")
            line = f_in.readline()
