#!/usr/bin/env python3

import sys

users = {}

line = sys.stdin.readline().rstrip()
while 0 < len(line):
    tokens = line.split("/")  # Extract user name, task and status
    user = tokens[0]
    tokens = ".".join(tokens).split(".")
    task = tokens[1] + ".py"
    state = tokens[3]

    if user in users:  # add new task or update state
        users[user][task] = state
    else:
        tasks = {task: state}  # add new user to users
        users[user] = tasks
    line = sys.stdin.readline().rstrip()

for user in users:
    count = 0
    for task in users[user]:
        if users[user][task] == "correct":
            count = count + 1
    print(user, count)
