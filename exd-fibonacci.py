#!/usr/bin/env python3

n = int(input())

fib_nums = [0, 1]

last = fib_nums[len(fib_nums) - 1]
sec_last = fib_nums[len(fib_nums) - 2]

next_num = last + sec_last
while next_num <= n:
    fib_nums.append(next_num)
    last = fib_nums[len(fib_nums) - 1]
    sec_last = fib_nums[len(fib_nums) - 2]
    next_num = last + sec_last

if n in fib_nums:
    print("yes")
else:
    print("no")
