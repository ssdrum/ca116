#!/usr/bin/env python3

n = int(input())

third_digit = n % 10
n = n // 10

second_digit = n % 10
n = n // 10

first_digit = n % 10
n = n // 10

print(first_digit)
print(second_digit)
print(third_digit)
