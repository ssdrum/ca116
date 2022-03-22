#!/usr/bin/env python3

tot_num_serv = 0
jobs = []

start_time = input()
while start_time != "end":
    jobs.append(int(start_time))
    curr_used_serv = 0

    i = 0
    while i < len(jobs):
        if int(start_time) <= jobs[i] + 1000:
            curr_used_serv = curr_used_serv + 1
            if tot_num_serv < curr_used_serv:
                tot_num_serv = curr_used_serv
        i = i + 1
    start_time = input()

print(tot_num_serv)
